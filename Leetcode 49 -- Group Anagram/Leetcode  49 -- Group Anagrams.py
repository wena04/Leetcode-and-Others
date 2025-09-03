# Leetcode 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        #Method 1: HashMap of charCount to the words that can make this anagram

        #mapping charCount to the list of Anagrams
        #key = unique charCounts for a certain word
        #value = list of strings that has that same charCount
        res = defaultdict(list) #make it so that there is a dictionary that stores lists

        for s in strs:
            count = [0]*26 # array with each index representing the count of different characters from a to z

            for c in s: #loop through the specific word/string in the list
                #ord takes the ASCII value of the current char we at
                count[ord(c)-ord("a")] += 1 
            
            #tuple since it is a immutable list
            res[tuple(count)].append(s) 
        
        return res.values()

        #time complexity: O(m*N*26) or just O(N)
        #space complexity: O(N)
        