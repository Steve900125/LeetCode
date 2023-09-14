# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        # First Part deal empty list
        # Return None
        if len(lists) == 0:
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

        # Condition: no None LinkList
        #  n range in -10 ^ 4 to 10 ^ 4
        hash_map = [ [] for _ in range(20000)]

        head = temp = ListNode()

        for k in range(len(lists)):
            while  lists[k] != None:
                # Reset index
                loc_in_hash = lists[k].val + 10000
                hash_map[loc_in_hash].append(lists[k])
                lists[k] = lists[k].next
        
        for target in range(len(hash_map)):
            if len(hash_map[target]) == 0 :
                continue
            
            for node in hash_map[target]:
                temp.next = node
                temp = temp.next

        return head.next