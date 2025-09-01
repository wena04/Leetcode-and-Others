# Leetcode 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Base case: empty node in front
        prev = None
        curr = head
        #keep running until base case
        while curr:
            #temp to store the current next value
            temp = curr.next
            #reverse the pointer to point the next value to prev
            curr.next = prev
            #make the previous value the current value now for the next iteration
            prev = curr
            #move to the next value to check
            curr = temp

        return prev

#time complexity: O(N)
#space complexity: O(1)

        
