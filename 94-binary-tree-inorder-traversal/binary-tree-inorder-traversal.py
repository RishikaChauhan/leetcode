# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls= []
        l,k=[],[]
        if root:
            l, k = [], []
            if root.left: l = self.inorderTraversal(root.left)
            ls.append(root.val)
            if root.right: k=self.inorderTraversal(root.right)
        p = (l if l else [])+ls+(k if k else [])
        return p
        # res = []

        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right)

        # helper(root)
        # return res