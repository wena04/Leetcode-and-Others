#!/usr/bin/env python3
import os, re, shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(".")
README = ROOT / "README.md"
BACKUP = ROOT / "README.backup.md"

SECTION_HEADERS = [
    "##### [Easy Problems]()",
    "#### [Medium Problems]()",
    "#### [Hard Problems]()",
]

TABLE_HEADER = (
    "| #   | Title | Solution | Time/Space Complexity | Methods/Notes | Date Completed |\n"
    "| --- | ----- | -------- | --------------------- | ------------- | -------------- |\n"
)

def read_existing():
    """Read existing README and parse rows into a dict keyed by problem id.
       Preserve section membership and the non-solution columns."""
    if not README.exists():
        return None, {}, set()

    text = README.read_text(encoding="utf-8")
    # Keep everything above the first known section as "preamble"
    # If none found, keep entire file as preamble.
    first_idx = min([text.find(h) for h in SECTION_HEADERS if h in text] or [len(text)])
    preamble = text[:first_idx].rstrip() + "\n\n"

    current_section = None
    problems = {}  # key: str(problem_id), val: dict with preserved cells + section name
    seen_sections = set()

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() in SECTION_HEADERS:
            current_section = line.strip()
            seen_sections.add(current_section)
            # Skip the two header lines that follow (header + separator) if present
            i += 1
            # Look ahead for table header start within next few lines
            # Not strictly necessary, but robust to slight variations
        elif current_section and line.startswith("|"):
            # Skip header/separator rows
            if "| ---" in line:
                i += 1
                continue
            # Parse row until a non-table line or next section
            row = line
            # Count columns by splitting on '|'
            cells = [c.strip() for c in row.strip().split("|")[1:-1]]
            if len(cells) >= 6:
                pid = cells[0]  # expected numeric like '1', but keep as str
                # Preserve everything except "Solution" (index 2)
                # cells: [# , Title, Solution, Complexity, Notes, Date]
                problems[str(pid)] = {
                    "section": current_section,
                    "title_cell": cells[1],
                    "solution_cell": cells[2],  # will be replaced/merged
                    "complexity_cell": cells[3],
                    "notes_cell": cells[4],
                    "date_cell": cells[5],
                }
        i += 1

    return preamble, problems, seen_sections


slugify_re_keep = re.compile(r"[^a-z0-9-]")

def best_effort_slug(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"\s+", "-", t)
    t = slugify_re_keep.sub("", t)
    return t

def find_leetcode_dirs():
    """Return list of (problem_id_str, title, folder_path) for Leetcode folders."""
    results = []
    for d in ROOT.iterdir():
        if not d.is_dir():
            continue
        name = d.name
        if not name.startswith("Leetcode "):
            continue
        # Accept "Leetcode <num> -- <title>" or "Leetcode <num>: <title>"
        m = re.match(r"^Leetcode\s+(\d+)\s*(?:--|:)\s*(.+)$", name)
        if not m:
            continue
        num = m.group(1)
        title = m.group(2).strip()
        results.append((num, title, d))
    # sort numerically by problem id
    results.sort(key=lambda x: int(x[0]))
    return results

def build_solutions_md(folder: Path) -> str:
    """Build the solutions cell content from files in folder (Python, then Java)."""
    links = []
    for ext, label in (("py", "Python"), ("java", "Java")):
        for f in sorted(folder.glob(f"*.{ext}")):
            rel = f.relative_to(ROOT).as_posix()
            # URL-encode spaces
            rel_enc = "/".join(quote(part) for part in rel.split("/"))
            links.append(f"[{label}]({rel_enc})")
    return " ".join(links) if links else ""

def render_table(rows):
    out = [TABLE_HEADER]
    out.extend(rows)
    return "".join(out)

def main():
    preamble, existing, seen_sections = read_existing()
    if preamble is None:
        # No README — make a minimal preamble
        preamble = (
            "# Anthony's Leetcode and Other Practice\n\n"
            "Using Python or Java to answer leet code and other problems to prep for tech interviews\n\n"
        )

    # Safety backup
    if README.exists():
        shutil.copyfile(README, BACKUP)

    # Scan filesystem
    leet_dirs = find_leetcode_dirs()

    # Buckets
    by_section = {s: [] for s in SECTION_HEADERS if s in seen_sections}
    unsorted_rows = []

    # Build/merge rows
    for num, title, folder in leet_dirs:
        # Construct a default title cell (but if existing title cell exists, keep it)
        slug = best_effort_slug(title)
        lc_url = f"https://leetcode.com/problems/{slug}/"
        default_title_cell = f"[{title}]({lc_url})"
        solutions_md = build_solutions_md(folder)

        # If problem exists in existing README, preserve all non-solution cells
        key = str(num)
        if key in existing:
            rowd = existing[key]
            title_cell = rowd["title_cell"] or default_title_cell
            # If old solution cell exists, replace with newly generated links (so it updates)
            solution_cell = solutions_md or rowd["solution_cell"]
            complexity_cell = rowd["complexity_cell"]
            notes_cell = rowd["notes_cell"]
            date_cell = rowd["date_cell"]
            section = rowd["section"]
        else:
            # New problem: create blank skeleton cells
            title_cell = default_title_cell
            solution_cell = solutions_md
            complexity_cell = ""
            notes_cell = ""
            date_cell = ""
            section = None  # will go to Unsorted

        row_md = f"| {num} | {title_cell} | {solution_cell} | {complexity_cell} | {notes_cell} | {date_cell} |\n"

        if section in by_section:
            by_section[section].append(row_md)
        else:
            unsorted_rows.append(row_md)

    # Build "Other Problems" table from non-Leetcode dirs
    other_rows = []
    for d in sorted([p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("Leetcode ")]):
        if d.name in {".git", "node_modules"} or d.name.startswith("."):
            continue
        # Solutions in folder root
        sols = []
        for f in sorted(d.glob("*")):
            if not f.is_file():
                continue
            label = {
                "py": "Python",
                "java": "Java",
                "md": "Markdown",
            }.get(f.suffix.lstrip("."), "File")
            rel = f.relative_to(ROOT).as_posix()
            rel_enc = "/".join(quote(part) for part in rel.split("/"))
            sols.append(f"[{label}]({rel_enc})")
        folder_name_enc = quote(d.name)
        other_rows.append(f"| {d.name} | {' '.join(sols)} |  |  |  |\n")

    # Recompose README
    out = [preamble.rstrip(), "\n"]
    # Print seen sections in the original order, with their tables (if any rows)
    for sec in SECTION_HEADERS:
        if sec in by_section and by_section[sec]:
            out.append(f"{sec}\n\n")
            out.append(render_table(by_section[sec]))

    # Unsorted Problems section for any new ones
    if unsorted_rows:
        out.append("\n#### [Unsorted Problems]\n\n")
        out.append(render_table(unsorted_rows))

    # Other Problems
    if other_rows:
        out.append("\n#### [Other Problems]\n\n")
        out.append(
            "| Name | Solution | Time/Space Complexity | Methods/Notes | Date Completed |\n"
            "| ---- | -------- | --------------------- | ------------- | -------------- |\n"
        )
        out.extend(other_rows)

    README.write_text("".join(out), encoding="utf-8")
    print("README.md updated ✔  (backup at README.backup.md)")

if __name__ == "__main__":
    main()
