# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        def dfs(root):
            if not root: return
            if root:
                path.append(str(root.val))
                if not root.left and not root.right:
                    res.append("->".join(path))
                else:
                    dfs(root.left)
                    dfs(root.right)
                path.pop()
        dfs(root)
        return res