# Leetcode 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #last pointer to start from end of final array
        last = m + n - 1

        #merge arrays in reverse order
        #run while both arr 
        while m > 0 and n > 0:
            #put the bigger value of the 2 arrays to the end
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else: 
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        #fill the rest of the array with values from nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        
        return nums1

#time complexity: O(N)
#space complexity: O(1)

        
