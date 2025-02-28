# Leetcode 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#Method: 2 pointers, swap to move unique ones to front
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #this way we can just start at index 1
        if len(nums) == 0:
            return 0
        left = 1 #keep track of the amount of unique int
        for right in range(1,len(nums)):
            #if the two values side by side is different then it's a unique int
            if nums[right - 1] != nums[right]:
                #set the last time we seen a duplicate to the unique value we found
                nums[left] = nums[right]
                #move counter/tracker to new place we could put unique value
                left += 1
        return left
        
#time complexity: O(N)
#space complexity: O(1)
