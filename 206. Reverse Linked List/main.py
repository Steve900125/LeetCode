# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # I miss that :(
        if head is None:
            return None
        
        # stack record front to end then pop end to relink
        stack = []

        # move the link list
        while head is not None:
            stack.append(head)
            head = head.next

        # get the end element to new header
        new_head = stack.pop()
        temp = new_head
        
        while len(stack):
            temp.next = stack.pop()
            temp = temp.next

        # Set the next of the last node to None
        temp.next = None
        # I miss that :(

        return new_head