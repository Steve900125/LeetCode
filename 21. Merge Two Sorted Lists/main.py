# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            cur_list1 = list1.next
            cur_list2 = list2
        else:
            head = list2
            cur_list1 = list1
            cur_list2 = list2.next

        temp = head 

        while cur_list1 and cur_list2 is not None:
            if cur_list1.val <= cur_list2.val:
                temp.next = cur_list1
                cur_list1 = cur_list1.next
            else:
                temp.next = cur_list2
                cur_list2 = cur_list2.next
            temp = temp.next
        
        if cur_list1 is not None and cur_list2 is None:
            temp.next = cur_list1
        if cur_list2 is not None and cur_list1 is None:
            temp.next = cur_list2
        
        return head
        





            

        

        pass