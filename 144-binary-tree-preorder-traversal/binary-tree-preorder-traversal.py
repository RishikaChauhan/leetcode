# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls= []
        l,k=[],[]
        if root:
            l, k = [], []
            if root.left: l = self.preorderTraversal(root.left)
            ls.append(root.val)
            if root.right: k=self.preorderTraversal(root.right)
        p = ls + (l if l else [])+(k if k else [])
        return p