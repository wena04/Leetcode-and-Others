# Leetcode 169: Majority Element
# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Method 1: Most common way
        #Time complexity: O(N)
        #Space complexity: O(N)
        #count the frequency of every character
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        #compare each frequency to the largest frequency right now 
        #update result accordingly
        result, big = 0, 0
        for key,value in freq.items():
            if value > big:
                result = key
                big = value
        
        return result

        #Method 2: special counting, only works since freq of majority element will have n/2
        #Time complexity: O(N)
        #Space complexity: O(1)
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else: 
                count -=1
        return res
        
