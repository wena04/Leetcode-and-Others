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

        # use enumerate to keep track of the index and indexies easily
        for value, key in enumerate(nums):
            searching = target - key
            if searching in seen:
                return [value, seen[searching]]
            else:
                seen[key] = value
        
        return

# time complexity: O(N)
# space complexity: O(N)
