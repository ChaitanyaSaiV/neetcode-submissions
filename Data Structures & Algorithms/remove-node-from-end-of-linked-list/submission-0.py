# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        lPointer = head
        rPointer = head
        while n > 0:
            print(rPointer.val)
            rPointer = rPointer.next
            n -= 1
        prev = None
        while rPointer is not None:
            prev = lPointer
            lPointer = lPointer.next
            rPointer = rPointer.next
            
        if prev is None:
            return head.next

        prev.next = lPointer.next

        return tail
