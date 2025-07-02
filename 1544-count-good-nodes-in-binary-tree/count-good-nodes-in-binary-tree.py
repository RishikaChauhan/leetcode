# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(node, mval):
            
            if not node: return 0
            res = 1 if node.val>=mval else 0
            mval = max(
                node.val, mval
            )
            res += dfs(node.left, mval)
            res += dfs(node.right, mval)
            return res
        return dfs(root, root.val)