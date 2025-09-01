#!/bin/bash

# Organize Leetcode solutions into folders

for f in Leetcode*.*; do
  # Skip if it's already a directory
  [ -d "$f" ] && continue

  # Extract problem number (first number after "Leetcode")
  num=$(echo "$f" | awk '{print $2}')

  # Extract title (everything after the number, strip extension)
  title=$(echo "$f" | sed -E 's/Leetcode [0-9]+ -- (.*)\.(py|java)/\1/' \
                 | sed -E 's/Leetcode [0-9]+: (.*)\.(py|java)/\1/')

  # Normalize separator to " -- "
  folder="Leetcode $num -- $title"

  # Create folder if missing
  mkdir -p "$folder"

  # Move file into folder
  mv "$f" "$folder/"
done
