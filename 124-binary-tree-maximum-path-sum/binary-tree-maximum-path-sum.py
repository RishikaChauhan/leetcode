# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            nonlocal sm
            if not root: return 0
            sm1 = max(dfs(root.left),0)
            
            sm2 = max(dfs(root.right),0)
            sm = max(sm, root.val+sm1+sm2)
            return root.val + max(sm1, sm2)
        sm = root.val
        dfs(root)
        return sm