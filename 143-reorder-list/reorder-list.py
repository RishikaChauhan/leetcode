# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        stack = []
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        temp = slow.next
        mid.next = None
        
        # print(temp)
        while temp:
            stack.append(temp)
            temp = temp.next
        nt = head
        # print(stack)
        while nt:
            t = nt.next
            if stack!= []:
                nt.next = stack.pop()
            else: break
            nt.next.next = t
            nt = t
        return head
