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
        hare, tortoise = head, dummy

        for i in range(n):
            hare = hare.next

        while(hare):
            hare = hare.next
            tortoise = tortoise.next
        tortoise.next = tortoise.next.next

        return dummy.next