# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        
        def dfs (node, lb, rb):
            if not node:
                return True
        
            if lb<node.val<rb:
                return dfs( node.left,lb, node.val) and dfs( node.right,node.val, rb)
            else: return False
        return dfs(node,lb = float('-inf'), rb=float('inf'))