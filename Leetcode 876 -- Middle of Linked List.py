# Leetcode 876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Method: slow fast pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slowpointer = head
        fastpointer = head
        while fastpointer is not None and fastpointer.next is not None:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
        
        return slowpointer
#time complexity: O(N)
#space complexity: O(1)
