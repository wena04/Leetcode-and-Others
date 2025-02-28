# Leetcode 102: Binary Tree Level Order Traversal 
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Method: BFS tree traversal
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        #to store final list
        results = []
        queue = deque()
        queue.append(root)
        #while queue is not empty, keep searching
        while queue:
            #length of the current level
            current_len = len(queue)
            levels = []
            #ensures that we are only searching the current level to add to levels
            for i in range(current_len):
                #pop the current code
                curr = queue.popleft()
                #if current is not null
                if curr:
                    #add current node to the current level list
                    levels.append(curr.val)
                    #notice these could be null, but add its children to be searched later
                    queue.append(curr.left)
                    queue.append(curr.right)
            if levels:
                results.append(levels)
        return results

#time complexity: O(N)
#space complexity: O(N)



        
