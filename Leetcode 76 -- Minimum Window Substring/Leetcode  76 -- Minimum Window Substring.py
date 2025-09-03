# Leetcode 76: Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        # Method 1: Sliding Window with Hashmaps
        # Have a freq count for the target string, and also a freq count for the current window. We shrink and expand the window only when we meet all the target freq/conditions (so when the freq count of each characters match exactly). 

        # 1. Preprocess target: Build a frequency map (target) for string t.
        # 2. Expand right pointer: Iterate through s, adding characters to the window map.
        # 3. Check validity: If a character’s count in window matches target, increase have.
        # 4. Shrink left pointer: When all requirements are satisfied (have == need), try moving left forward to minimize the window, updating the best result if smaller.
        # 5. Update result: Keep track of the minimum-length valid window seen.
        # 6. Return slice: Extract substring from s using stored indices.

        resultlen = float('inf') # minimum length of window so far
        left, resultleft = 0, 0 # left pointer spot, start of minimum window so far
        target = Counter(t) # makes hashmap of freq of char for target string
        window = Counter() # hashmap to track freq of char in our current window
        have, need = 0, len(target) # number of unique characters we have currently VS need to satisfy 

        # use enumerate to get the index and value of character in string s
        for index, value in enumerate(s):
            window[value] += 1 # increase current char's freq count by 1
            # check if current character meets target criteria of current character
            if value in target and window[value] == target[value]:
                have += 1

            # if freq of have and need are the same, start shrinking window
            while have == need:
                # current window length is minimum then update the lengths
                if index-left+1 < resultlen:
                    resultlen = index-left+1
                    resultleft = left
                # pop current character out and check if it still satisfies the character's condition
                leftchar = s[left]
                window[leftchar] -= 1
                if leftchar in target and window[leftchar] < target[leftchar]:
                    have -= 1
                # shrink window
                left += 1
        # return final result
        return "" if resultlen == float('inf') else s[resultleft:resultleft + resultlen]

#time complexity: O(N+m) or just O(N)
#space complexity: O(N)
