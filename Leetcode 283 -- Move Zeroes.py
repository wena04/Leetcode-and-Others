# Leetcode 283: Move Zeroes 
# https://leetcode.com/problems/move-zeroes/description/

# two pointers, swap to put valid numbers in front
class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        for i in range(len(nums) - left):
            nums[i + left] = 0
        
        return nums

  #time complexity: O(N)
  #space complexity: O(1)
