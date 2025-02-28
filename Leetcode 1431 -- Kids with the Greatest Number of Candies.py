# Leetcode 1431: 
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

#method: find max candy in beginning, then iterate through list to check
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candy = max(candies)
        answer = list()
        for i in range(len(candies)):
            if candies[i] + extraCandies >= candy:
                answer.append(True)
            else: 
                answer.append(False)

        return answer

#time complexity: O(N)
#space complexity: O(N)
