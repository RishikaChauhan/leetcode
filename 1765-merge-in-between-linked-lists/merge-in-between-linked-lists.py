# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr= list1
        for i in range(a-1):
        # while curr and curr.val != a:
            curr = curr.next
        # print(curr)
        r = curr.next

        for i in range(b-a+1):
        # while r and r.val != b:
            r = r.next
        # print(r)
        curr.next = list2
        while curr and curr.next:
            curr = curr.next
        
        # print(curr)
        curr.next = r
        return list1