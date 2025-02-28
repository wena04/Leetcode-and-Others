# Leetcode 128: Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# idea: try to find the start of each sequence and compare each length of a sequence by seeing if the rest of the sequence exists in a set 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        timeline = set(nums) # timeline to contain all numbers, removing duplicates first
        answer = 0

        for i in timeline: #for every number in i
            if (i - 1) not in timeline: # check if it is start of a sequence
                length = 1 # the current sequence's length is 1
                while (i + length) in timeline: # continue searching for rest of the numbers in the sequence
                    length += 1
                answer = max(answer, length) # check if the current sequence is the longest one so far
        return answer

# time complexity: O(n)        
# memory: O(n)
