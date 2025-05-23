# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        dummy = head
        def middle(head):
            fast = slow = head
            prev = slow
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow  = slow.next
            
            if prev: prev.next = None
            return slow
        mid = middle(head)

        res = TreeNode(mid.val)
        if mid ==head: return res
        res.left = self.sortedListToBST(head)
        res.right = self.sortedListToBST(mid.next)
        return res
