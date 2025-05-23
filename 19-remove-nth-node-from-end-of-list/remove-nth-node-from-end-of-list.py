# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        dummy = res = ListNode()
        dummy.next = head

        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            res = res.next
        res.next = res.next.next
        return dummy.next
