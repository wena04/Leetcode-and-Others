# Leetcode 1: Two Sum
# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap to keep track of what we seen before
        seen = {}

        # use enumerate to keep track of the index and indices/values of nums easily: 
        # enumerate function gives you a pair of (index, values) of the variable your iterating through
        for i, value in enumerate(nums):
            searching = target - value
            if searching in seen:
                return [i, seen[searching]]
            seen[value] = i
        
        return []

# time complexity: O(N)
# space complexity: O(N)
