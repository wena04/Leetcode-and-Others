# Leetcode 27: Remove Element
# https://leetcode.com/problems/remove-element/

#swapping elements to front of array inplace 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        # swapping the valid num to the front of the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
      
  # time complexity: O(N)
  # space complexity: O(1)

        
