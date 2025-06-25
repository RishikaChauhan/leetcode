# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            lh, rh = 0,0
            if not node: return [True, 0]
            # if node.left and not node.right: return [False, 0]
            # if not node.left and node.right: return [False, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            if left[0] and right[0] and abs(left[1]-right[1])<=1: 
                return [True, 1+max(left[1], right[1])]
            return [False,0]
        return dfs(root)[0]