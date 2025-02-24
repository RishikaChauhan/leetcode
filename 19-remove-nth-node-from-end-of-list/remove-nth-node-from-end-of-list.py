# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        res = ListNode(0)
        res.next = head
        curr = res
        while i<n:
            head = head.next
            i=i+1
        while head:
            head = head.next
            curr = curr.next
        curr.next = curr.next.next
        return res.next