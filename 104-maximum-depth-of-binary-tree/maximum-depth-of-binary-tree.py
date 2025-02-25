# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l = 0
        # def dfs(l,root):
        #     if not root: l=0
        #     if node.left or node.right:
        #     l+=1
        #     return l
        if not root:return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        

        