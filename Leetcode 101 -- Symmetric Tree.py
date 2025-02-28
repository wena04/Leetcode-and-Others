# Leetcode 101: Symmetric Tree 
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        #need another method for to pass in 2 TreeNodes
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if (left == None and right == None):
            return True
        if (left == None or right == None):
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)    
#time complexity: O(N)
#space complexity: O(1) or just O(h) where h is height of tree
