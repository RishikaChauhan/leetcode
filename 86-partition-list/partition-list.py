# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = reshead = ListNode()
        res1 = res1head =  ListNode()

        while head:
            if head.val >= x:
                res1.next = head
                # res1.next = None
                res1 = res1.next
                # res1.next = None
            elif head.val<x:
                res.next = head
                res = res.next
            head = head.next
        # print(res1head)
        res1.next = None
        # print(reshead, res)
        res.next = res1head.next
        return reshead.next