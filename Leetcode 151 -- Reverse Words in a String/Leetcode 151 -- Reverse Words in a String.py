# Leetcode 151: Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

#method 1: use python built in ones o remove spaces -> use queue to flip word
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        #remove leading spaces
        while left <= right and s[left] == " ":
            left += 1
        #remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)
        # use python's built in function, still O(N) but in place
        return " ".join(reversed(s.split()))
#time complexity: O(N)
#space complexity: O(N)


        
