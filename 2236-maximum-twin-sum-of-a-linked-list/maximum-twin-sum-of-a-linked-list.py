# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []
        ans = 0
        if fast and fast.next and fast.next.next == None: return fast.val+fast.next.val
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next
        # print(stack)
        # print(slow)
        while stack:
            # print(slow.val, stack[-1])
            ans = max(ans, stack[-1]+slow.val)
            slow = slow.next
            stack.pop()

        return ans
        