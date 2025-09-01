# Leetcode 3: Longest Substring without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method 1: sliding window method
        left = answer = 0
        seen = set()

        for right in range(len(s)):
            # checking for duplicates in substring
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            #updating the answer
            answer = max(answer, right - left + 1)
        
        return answer
        # time complexity: O(N)
        # space complexity: O(N)

        
