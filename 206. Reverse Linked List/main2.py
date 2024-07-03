from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse 
        cur = None
        prev = None

        while head is not None:
            prev = head
            if prev.next is not None:
                cur = prev.next
                cur.next = prev
            head = head.next
        return cur
            