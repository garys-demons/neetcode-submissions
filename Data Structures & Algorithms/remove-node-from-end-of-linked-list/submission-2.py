# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        hare, tort = head, dummy

        for i in range(n):
            hare = hare.next

        while hare:
            hare = hare.next
            tort = tort.next

        tort.next = tort.next.next
        return dummy.next