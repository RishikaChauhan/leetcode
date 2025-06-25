# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(l,r):
            if not l and r: return False
            if not r and l: return False
            if not l and not r: return True
            if l and r:
                return l.val ==r.val and dfs(l.left, r.left) and dfs(l.right, r.right)
        return dfs(p,q)