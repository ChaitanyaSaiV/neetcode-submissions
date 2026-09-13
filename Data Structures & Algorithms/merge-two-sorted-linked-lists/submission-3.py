# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        c1 = list1
        c2 = list2

        if c1.val < c2.val:
            tail = c1
            c1 = c1.next
        else:
            tail = c2
            c2 = c2.next
        
        dummyHead = tail
        
        while c1 is not None and c2 is not None:
            if c1.val < c2.val:
                tail.next = c1
                tail = tail.next
                c1 = c1.next
            else:
                tail.next = c2
                tail = tail.next
                c2 = c2.next
        
        if c1 is None:
            tail.next = c2
        else:
            tail.next = c1

        return dummyHead
