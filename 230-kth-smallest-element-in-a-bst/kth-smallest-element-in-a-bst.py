# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        res = []
        def inorder(root):
            nonlocal res
            if root:
                # return res
                if root.left: inorder(root.left)
                res.append(root.val)
                if root.right: inorder(root.right)
            return res
        res = inorder(root)
        print(res)
        return res[k-1]