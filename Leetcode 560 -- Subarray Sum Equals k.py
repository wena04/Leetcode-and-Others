# Leetcode 560: Subarray Sum Equals k
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        count = {0:1} #to count freq of subarry's sum we seen before
        currSum = 0 #to count the current sum
        answer = 0
        for i in range(len(nums)):
            currSum += nums[i] #calc sum from index 0 up to current index
            answer += count.get(currSum - k, 0) #update answer to freq of times we seen
            count[currSum] = count.get(currSum, 0) + 1 #count current sum to what we have seen before
            
        return answer

        #line 12 your esstentially adding num of ways you can get the curr sum based on what we have seen before

#time complexity: O(N)
#space complexity: O(N)
            
        
                
        
