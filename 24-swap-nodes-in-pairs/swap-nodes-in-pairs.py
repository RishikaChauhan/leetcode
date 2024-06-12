# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        ans = []
        for i in range(0, len(lst),2):
            val = lst[i:i+2]
            ans+=val[::-1]
        final =ListNode(0)
        temp = final
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next
        return final.next

