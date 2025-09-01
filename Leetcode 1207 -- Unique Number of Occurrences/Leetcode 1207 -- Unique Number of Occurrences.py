# Leetcode 1207: Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

#Method: count the frequency of everything and compare with original's length
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0)+1

        return len(freq) == len(set(freq.values()))
        
#time complexity: O(N)
#space complexity: O(N)
