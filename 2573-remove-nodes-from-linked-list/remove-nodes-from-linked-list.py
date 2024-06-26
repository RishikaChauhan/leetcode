# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1].val<head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        ans  = ListNode(-1)
        temp = ans
        for node in stack:
            temp.next = node
            temp = temp.next
        return ans.next