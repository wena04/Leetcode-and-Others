# Leetcode 32: Longest Valid Parentheses 
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        # initialize stack to contain a -1 for valid calculations later on
        stack = [-1] # stack to count index of latest '('

        for i in range(len(s)):
            if (s[i] == '('):
                stack.append(i) # add the index of the latest '(' seen
            else: 
                stack.pop() # seen a ')' so pop one index from stack
                if not stack: # if stack is empty because of that
                    stack.append(i) # reset the stack by adding back the current index
                else: # if stack is not emtpy
                    # see if the last valid parentheses substring we seen is larger than our current one
                    answer = max(answer, i - stack[-1]) # update answer
        
        return answer

        #By storing indices instead of characters, we can compute valid lengths by taking differences between indices. We start with -1 in the stack to handle cases where the sequence starts at index 0
