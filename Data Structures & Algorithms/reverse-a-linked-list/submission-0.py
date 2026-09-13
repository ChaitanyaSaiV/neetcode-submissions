# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        dummy = None
        prev = dummy

        current = head

        while current is not None:
            cNext = current.next
            current.next = prev
            prev = current
            current = cNext
        
        return prev