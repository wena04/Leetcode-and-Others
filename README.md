# Anthony's Leetcode and Other Practice

Using Python or Java to answer leet code and other problems to prep for tech interviews
##### [Easy Problems]()

| #   | Title | Solution | Time/Space Complexity | Methods/Notes | Date Completed |
| --- | ----- | -------- | --------------------- | ------------- | -------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](Leetcode%201%20--%20Two%20Sum/Leetcode%201%20--%20Two%20Sum.py) [Java](Leetcode%201%20--%20Two%20Sum/Leetcode%201%20--%20Two%20Sum.java) | O(N)/O(N) | Hashmap to see if seen the target num subtracted by current number -> return value if have | May 25, 2024 |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Python](Leetcode%2014%20--%20Longest%20Common%20Prefix/Leetcode%2014%20--%20Longest%20Common%20Prefix.py) [Java](Leetcode%2014%20--%20Longest%20Common%20Prefix/Leetcode%2014%20--%20Longest%20Common%20Prefix.java) | O(N)/O(M) for both | set empty string, iterate through all the strings at once (need 2 for loops), return when i == len(s) or s[i] != strs[0][i] | Apirl 04, 2024 |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Java](Leetcode%2021%20--%20Merge%20Two%20Sorted%20Lists/Leetcode%2021%20--%20Merge%20Two%20Sorted%20Lists.java) | O(N)/O(N) | Creating a new linked list and add in required order | June 5, 2024 |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | [Python](Leetcode%20118%20--%20Pascal%27s%20Triangle/Leetcode%20118%20--%20Pascal%27s%20Triangle.py) [Java](Leetcode%20118%20--%20Pascal%27s%20Triangle/Leetcode%20118%20--%20Pascal%27s%20Triangle.java) | O(N^2)/O(N^2) | Dynamic Programming -> every row is a list/array itself -> recursive calling itself to use previous row to calculate current row | May 25, 2024 |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Java](Leetcode%20125%20--%20Valid%20Palindrome/Leetcode%20125%20--%20Valid%20Palindrome.java) | O(N)/O(1) | Two pointers, start at each end and compare | June 1, 2024 |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](Leetcode%20206%20--%20Reverse%20Linked%20List/Leetcode%20206%20--%20Reverse%20Linked%20List.py) [Java](Leetcode%20206%20--%20Reverse%20Linked%20List/Leetcode%20206%20--%20Reverse%20Linked%20List.java) | M1: O(N)/O(1)</br>M2: O(N)/O(N) | M1: Iteratively M2:Recursively | June 5, 2024 |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](Leetcode%20217%20--%20Contains%20Duplicate/Leetcode%20217%20--Contains%20Duplicate.py) | M1: O(N^2)/O(1)</br>M2: O(NlogN)/O(logN) </br>M3: O(N)/O(N) | M1: Brute Force</br>M2: sort array first, compare adjacent elements</br>M3: put elements into HashMap -> containsKey then return true, else false | May 25, 2024 |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](Leetcode%20242%20--%20Valid%20Anagram/Leetcode%20%20242%20--%20Valid%20Anagram.py) | M1: O(N)/O(N)</br>M2: O(NlogN)/O(1) but could also be said to be O(N) for space | M1: using Hashmap to count number of each character</br>M2: sort the string first | May 26, 2024 |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | [Java](Leetcode%20344%20--%20Reverse%20String/Leetcode%20344%20--%20Reverse%20String.java) | O(N)/O(1) | Two pointers, start at each end and swap characters | June 1, 2024 |
| 671 | [Second Minimum Node in a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) | [Java](Leetcode%20671%20--%20Second%20Minimum%20Node%20In%20a%20Binary%20Tree/Leetcode%20671%20--%20671.%20Second%20Minimum%20Node%20In%20a%20Binary%20Tree.java) | O(N)/O(N) | DFS -- preorder traversal but custom towards this special kind of tree -> think case by case | Apirl 23, 2024 |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Java](Leetcode%20746%20--%20Min%20Cost%20Climbing%20Stairs/Leetcode%20746%20--%20Min%20Cost%20Climbing%20Stairs.java) | O(N)/O(1) | DP -> base case first two steps -> loop curr = cost[i] + min(first,second), first = second, second = curr | Apirl 20, 2024 |
#### [Medium Problems]()

| #   | Title | Solution | Time/Space Complexity | Methods/Notes | Date Completed |
| --- | ----- | -------- | --------------------- | ------------- | -------------- |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Java](Leetcode%2011%20--%20Container%20With%20Most%20Water/Leetcode%2011%20--%20Container%20With%20Most%20Water.java) | O(N)/O(1) | two pointers, starting at opposite ends, move smaller pointer after testing area | June 5, 2024 |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Java](Leetcode%2033%20--%20Search%20in%20Rotated%20Sorted%20Array/Leetcode%2033%20--%20Search%20in%20Rotated%20Sorted%20Array.java) | O(logN)/O(1) | binary search | June 5, 2024 |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python](Leetcode%2049%20--%20Group%20Anagram/Leetcode%20%2049%20--%20Group%20Anagrams.py) | O(N)/O(N)) | HashMap of charCount to the words that can make this anagram | May 31, 2024 |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | [Java](Leetcode%20143%20--%20Reorder%20List/Leetcode%20143%20--%20Reorder%20List.java) | O(N)/O(N) | two pointers, one at each end but with linked lists | June 5, 2024 |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Python](Leetcode%20347%20--%20Top%20K%20Frequent%20Elements/Leetcode%20347%20--%20Top%20K%20Frequent%20Elements.py) | M1: O(N)/O(N)</br>M2: O(NlogK)/O(N) | M1: Bucket Sort + HashMap and then loop through for highest frequencies </br> M2: Heap/PQ that sort by freq of each quarter, output first k elements | May 31, 2024 </br> Feb 24, 2025 |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | [Python](Leetcode%20743%20--%20Network%20Delay%20Times/Leetcode%20%20743%20--%20Network%20Delay%20Time.py) | O(NLogN)/O(N) </br>O(E\*logV) in terms of edges & vertex) | Dikjstra's Algorithm using MinHeap + stack to visit all nodes and see shortest path/weight | May 20, 2024 |
| 912 | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | [Java](Leetcode%20912%20--%20Sort%20an%20Array/Leetcode%20912%20--%20Sort%20an%20Array.java) | O(NLogN)/O(logN) | merge sort | May 20, 2024 |
#### [Hard Problems]()

| #   | Title | Solution | Time/Space Complexity | Methods/Notes | Date Completed |
| --- | ----- | -------- | --------------------- | ------------- | -------------- |
| 2781 | [Length of the Longest Valid Substring](https://leetcode.com/problems/length-of-the-longest-valid-substring/) | [Java](Leetcode%202781%20--%20Length%20of%20the%20Longest%20Valid%20Substring/Leetcode%202781%20--%20Length%20of%20the%20Longest%20Valid%20Substring.java) | O(N \* maxlengthofforbidden^2)/O(sum of forbidden words length) | Sliding Window + brute Force | June 1, 2024 |

#### [Unsorted Problems]

| #   | Title | Solution | Time/Space Complexity | Methods/Notes | Date Completed |
| --- | ----- | -------- | --------------------- | ------------- | -------------- |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](Leetcode%203%20--%20Longest%20Substring%20Without%20Repeating%20Characters/Leetcode%203%20--%20Longest%20Substring%20Without%20Repeating%20Characters.py) [Java](Leetcode%203%20--%20Longest%20Substring%20Without%20Repeating%20Characters/Leetcode%203%20--%20Longest%20Substring%20Without%20Repeating%20Characters.java) |  |  |  |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |  |  |  |  |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](Leetcode%2026%20--%20Remove%20Duplicates%20from%20Sorted%20Array/Leetcode%2026%20--%20Remove%20Duplicates%20from%20Sorted%20Array.py) |  |  |  |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | [Python](Leetcode%2027%20--%20Remove%20Element/Leetcode%2027%20--%20Remove%20Element.py) |  |  |  |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | [Python](Leetcode%2032%20--%20Longest%20Valid%20Parentheses/Leetcode%2032%20--%20Longest%20Valid%20Parentheses.py) |  |  |  |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [Python](Leetcode%2088%20--%20Merge%20Sorted%20Array/Leetcode%2088%20--%20Merge%20Sorted%20Array.py) |  |  |  |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | [Python](Leetcode%20101%20--%20Symmetric%20Tree/Leetcode%20101%20--%20Symmetric%20Tree.py) |  |  |  |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](Leetcode%20102%20--%20Binary%20Tree%20Level%20Order%20Traversal/Leetcode%20102%20--%20Binary%20Tree%20Level%20Order%20Traversal.py) |  |  |  |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](Leetcode%20104%20--%20Maximum%20Depth%20of%20Binary%20Tree/Leetcode%20104%20--%20Maximum%20Depth%20of%20Binary%20Tree.py) |  |  |  |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](Leetcode%20128%20--%20Longest%20Consecutive%20Sequence/Leetcode%20128%20--%20Longest%20Consecutive%20Sequence.py) |  |  |  |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [Python](Leetcode%20151%20--%20Reverse%20Words%20in%20a%20String/Leetcode%20151%20--%20Reverse%20Words%20in%20a%20String.py) |  |  |  |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | [Java](Leetcode%20155%20--%20Min%20Stack/Leetcode%20155%20--%20Min%20Stack.java) |  |  |  |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | [Python](Leetcode%20169%20--%20Majority%20Element/Leetcode%20169%20--%20Majority%20Element.py) |  |  |  |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | [Python](Leetcode%20203%20--%20Remove%20Linked%20List%20Elements/Leetcode%20203%20--%20Remove%20Linked%20List%20Elements.py) |  |  |  |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Python](Leetcode%20283%20--%20Move%20Zeroes/Leetcode%20283%20--%20Move%20Zeroes.py) |  |  |  |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | [Python](Leetcode%20409%20--%20Longest%20Palindrome/Leetcode%20409%20--%20Longest%20Palindrome.py) |  |  |  |
| 560 | [Subarray Sum Equals k](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](Leetcode%20560%20--%20Subarray%20Sum%20Equals%20k/Leetcode%20560%20--%20Subarray%20Sum%20Equals%20k.py) |  |  |  |
| 622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | [Java](Leetcode%20622%20--%20Design%20Circular%20Queue/Leetcode%20622%20--%20Design%20Circular%20Queue.java) |  |  |  |
| 876 | [Middle of Linked List](https://leetcode.com/problems/middle-of-linked-list/) | [Python](Leetcode%20876%20--%20Middle%20of%20Linked%20List/Leetcode%20876%20--%20Middle%20of%20Linked%20List.py) |  |  |  |
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | [Python](Leetcode%201071%20--%20Greatest%20Common%20Divisor%20of%20Strings/Leetcode%201071%20--%20Greatest%20Common%20Divisor%20of%20Strings.py) |  |  |  |
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | [Python](Leetcode%201207%20--%20Unique%20Number%20of%20Occurrences/Leetcode%201207%20--%20Unique%20Number%20of%20Occurrences.py) |  |  |  |
| 1431 | [Kids with the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | [Python](Leetcode%201431%20--%20Kids%20with%20the%20Greatest%20Number%20of%20Candies/Leetcode%201431%20--%20Kids%20with%20the%20Greatest%20Number%20of%20Candies.py) |  |  |  |
| 1657 | [-- Determine if Two Strings Are Close](https://leetcode.com/problems/---determine-if-two-strings-are-close/) | [Python](Leetcode%201657%3A%20--%20Determine%20if%20Two%20Strings%20Are%20Close/Leetcode%201657%3A%20Determine%20if%20Two%20Strings%20Are%20Close.py) |  |  |  |
| 1768 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | [Python](Leetcode%201768%20--%20Merge%20Strings%20Alternately/Leetcode%201768%20--%20Merge%20Strings%20Alternately.py) |  |  |  |
| 2095 | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) | [Python](Leetcode%202095%20--%20Delete%20the%20Middle%20Node%20of%20a%20Linked%20List/Leetcode%202095%20--%20Delete%20the%20Middle%20Node%20of%20a%20Linked%20List.py) |  |  |  |

#### [Other Problems]

| Name | Solution | Time/Space Complexity | Methods/Notes | Date Completed |
| ---- | -------- | --------------------- | ------------- | -------------- |
| UW Programming Competition 2024 -- N. Numerology | [File](UW%20Programming%20Competition%202024%20--%20N.%20Numerology/Problem%20Statement%20Quesiton%20N.png) [Python](UW%20Programming%20Competition%202024%20--%20N.%20Numerology/UW%20Programming%20Competition%202024%20--%20N.%20Numerology.py) |  |  |  |
