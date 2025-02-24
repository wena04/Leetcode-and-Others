# Leetcode 347: Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #Method 1: Bucket Sort

        count = {} #using a HashMap to count the frequency of a unique number in the List[int] passed in
        #we just have to make this about the size of our input + 1
        freq = [[] for i in range(len(nums)+1)] #index in freq is the frequency a value has appeared before and each will contain a list that contains the unique values with that key

        for n in nums:
            count[n] = 1 + count.get(n,0) #counting key:value pair of unique number:frequency of the number
        for n, c in count.items(): #for all the keys value pairs in the HashMap (using the .items() function), for all the key n and value c
            freq[c].append(n) #add the key into the bucket with index of the frequency

        res = [] #creating the final array that we are going to return
        for i in range(len(freq)-1,0,-1): #looping through in desc order starting from the last frequency
            for n in freq[i]: 
                res.append(n) #add all the unique numbers inside of the list inside that bucket
                if len(res) == k: #stop when we have the top k values
                    return res

        #time complexity: O(N)
        #space complexity: O(N)

        #Method 2: PQ/Heap sort

        #priority queue to return most frequent elements
        heap = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        for key, value in freq.items():
            #add into key, sort by freq
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the least frequent ones

        # Extract top k elements from heap
        return [key for value, key in heap]  # Extract keys only
    
        #Time Complexity: O(Nlogk)
        #Space Complexity: O(N)

        
        