# Leetcode 1657: Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

#Method: count freq and then make sure the freq matches 2 conditions
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        #counting frequency of each character in the list
        freq1 = {}
        freq2 = {}
        for i in range(len(word1)):
            freq1[word1[i]] = freq1.get(word1[i], 0) + 1
            freq2[word2[i]] = freq2.get(word2[i], 0) + 1

        # Condition 1: Both words must contain the same unique characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        freq1_count = {}
        freq2_count = {}
        # Condition 2: The frequency counts must match
        # Ex: how many times the freq of 2 appears in freq1 & freq2
        for i in freq1.values():
            freq1_count[i] = freq1_count.get(i,0) + 1
        
        for i in freq2.values():
            freq2_count[i] = freq2_count.get(i,0) + 1

        return freq1_count == freq2_count

#time complexity: O(N)
#space complexity: O(1) cuz the set will only be 26 letters in the alphabet
        

        
