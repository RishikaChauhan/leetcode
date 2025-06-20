# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        def dfs(node):
            h =node
            if not node: return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left:
                # temp = r
                node.right = node.left
                node.left = None
                while node.right:
                    node = node.right
                node.right=r
            return h
        head = dfs(root)
        return root
        