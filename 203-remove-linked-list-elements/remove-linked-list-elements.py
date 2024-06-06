# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val ==val:
            head = head.next
        pre = ListNode()
        pre.next = head
        curr = head
        while curr:
            nxt = curr.next
            if curr.val == val:
                pre.next  = nxt
            else:
                pre = curr
            curr = nxt
        return head