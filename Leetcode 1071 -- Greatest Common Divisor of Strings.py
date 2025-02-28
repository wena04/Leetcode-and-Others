# Leetcode 1071: Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)

        #function to check if substring can form both strings
        def isDivisor(l):
            #check if substring length can even make up both of the strings
            if len1 % l or len2 % l:
                return False
            #see how many times this substring need to create each string
            f1, f2 = len1 // l, len2 // l
            #check if can make this substring based on this
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
        
        #want to test substring from the largest substring possible
        for l in range(min(len1,len2),0,-1):
            if isDivisor(l):
                return str1[:l]
        
        return ""

#time complexity: O(min(m*n)*(n+m))
#space complexity: O(1)



        
        

