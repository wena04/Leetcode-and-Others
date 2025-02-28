# Leetcode 1768: Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

#Method: take the shorter string to loop, add each char of each string to a result string
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer = ""
        if len(word1) >= word2:
            shorter = len(word2)
            longer = word1
        else: 
            shorter = len(word1)
            longer = word2
        
        for i in range(shorter):
            if i < len(word1):
                answer += word1[i]
            if i < len(word2):
                answer += word2[i]

        for i in range(len(longer) - shorter):
            answer += longer[shorter + i]

        return answer

#time complexity: O(N)
#space complexity: O(N)
