//Leetcode 242: Valid Anagram
//https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Method 1: HashMaps counting the number of each character in string and see if they match
        return Counter(s) == Counter(t) # does the same thing as the bottom, just a function that does it for us

        if len(s) != len(t): return False #base case, if the 2 strings are just different length
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # the get method provides default value of 0 if s[i] no exist
            countT[t[i]] = 1 + countT.get(t[i],0)
        for j in countS:
            if countS[j] != countT.get(j,0): return False # has to use .get since letter could be N/A in one of the words, which is 0
        return True

        #time complexity: O(N) or technically both O(s+t)
        #space complexity: O(N)

        #Method 2: saving memory by sorting the arrays but time complexity might be different
        return sorted(s) == sorted(t)

        #time complexity: O(NlogN)
        #time complexity: O(N) but usually in interview assume doesn't take up any extra space so O(1)
