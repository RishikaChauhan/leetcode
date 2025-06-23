# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= [0]
        def dfs(root):
            if not root: return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(2+left+right, res[0])
            return 1+max(left, right)
        dfs(root)
        return res[0]
        # res = 0

        # def dfs(node):
        #     if not node: return -1
        #     l,r = dfs(node.left),dfs(node.right)
        #     res = max(res, l+r+2)
        #     return 1+max(l,r)            

        # return dfs(root)