# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = res = ListNode(0)
        
        def mer_two_list(l1, l2):
            node  = ListNode(0)
            ans = node
            while l1 and l2:
                if l1.val>l2.val:
                    node.next = l2
                    l2 = l2.next
                
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            if l1:
                node.next= l1
            else:
                node.next = l2
            return ans.next

        if not lists or len(lists) == 0:
            return None
        l1 = lists[0]
        for i in range(1, len(lists)):
            # print(l1)
            l1 = mer_two_list(l1, lists[i])
            
        return l1
