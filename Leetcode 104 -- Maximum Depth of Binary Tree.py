# Leetcode 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        #Method 1: DFS
        #base case is that our root is null
        if root == None:
            return 0
        #other base case is just 1 + either the max depth in left or right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#time complexity: O(N)
#space complexity: O(N)
