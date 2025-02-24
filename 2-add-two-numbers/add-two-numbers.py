# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = total = 0
        l3 = ListNode(0)
        res = l3
        while (l1 or l2) or carry!=0:
            total = carry

            if l1:
                total+= l1.val
                l1 = l1.next
            if l2: 
                total+= l2.val
                l2 = l2.next
            num = total%10
            carry = total//10
            l3.next = ListNode(num)
            l3 = l3.next
        return res.next
