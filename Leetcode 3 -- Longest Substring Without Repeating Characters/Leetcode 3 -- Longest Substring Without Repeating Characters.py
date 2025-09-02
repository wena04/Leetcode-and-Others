# Leetcode 3: Longest Substring without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method 1: sliding window method

        #using hashset
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

        #using hashmap
        left = answer = 0
        seen = {}
        #keep moving left pointer until window is valid
        #enumerate gives us pair of (current index, value at current index)
        for right_index, value in enumerate(s):
            #if we seen this value before, and value is in our window
            while value in seen and seen[value] >= left:
                #move the window to place we last seen the value
                left = seen[value] + 1
            #update last time we seen value
            seen[value] = right_index
            #update answer by checking if current window is larger than previous window
            answer = max(answer,right_index-left+1)
        return answer

        # time complexity: O(N)
        # space complexity: O(N)

        
