# Leetcode 2095: Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Method: slow fast pointer
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        
        slowpointer = head
        fastpointer = head
        prev = None

        while fastpointer and fastpointer.next:
            prev = slowpointer
            fastpointer = fastpointer.next.next
            slowpointer = slowpointer.next
        
        prev.next = prev.next.next
        return head

#time complexity: O(N)
#space complexity: O(1)
    
