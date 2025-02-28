# Leetcode 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

#Method: use a stack to keep track of open parentheses, pop everytime see end parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen = []
        for c in s:
            if c == '(':
                seen.append(')')
            elif c == '{':
                seen.append('}')
            elif c == '[':
                seen.append(']')
            elif seen and seen[-1] == c: 
                seen.pop()
            else: 
                return False

        return not seen 
#time complexity: O(N)
#space complexity: O(N)
