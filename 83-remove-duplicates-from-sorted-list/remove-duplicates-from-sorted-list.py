# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # pre = ListNode()
        # pre.next = head
        curr = head
        while curr:
            while curr.next and curr.next.val ==curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
        #     if curr.val == pre.val:
        #         pre.next = curr.next
        #     else:
        #         pre = curr
        #     curr = curr.next
        # return head