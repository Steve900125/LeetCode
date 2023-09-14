# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        # First Part deal empty list
        n_head = len(lists)

        # Return None
        if n_head == 0:
            return None
            
        all_None = True
        fix_remove = 0
        for k in range(len(lists)):

            if lists[k - fix_remove] != None:
                all_None = False
            else :
                # remove empty
                del lists[k - fix_remove]
                fix_remove += 1

        if all_None :
            return None

        head = temp = ListNode()

        # Rank the number
        while len(lists) != 0 :
            minum = lists[0]
            minum_i = 0
            for i in range(len(lists)):
                if minum.val > lists[i].val:
                    minum = lists[i]
                    minum_i = i
            
            temp.next = minum
            lists[minum_i] = minum.next
            temp = temp.next

            if lists[minum_i] == None:
                del lists[minum_i]
        return head.next

