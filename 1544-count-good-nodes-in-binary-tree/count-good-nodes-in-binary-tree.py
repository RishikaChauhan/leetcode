# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # maxvalue = 0
        def dfs(node, maxvalue):
            if not node: return 0
            res = 1 if node.val>=maxvalue else 0
            maxvalue = max(node.val, maxvalue)
            res += dfs(node.left, maxvalue)
            res += dfs(node.right, maxvalue)
            return res
        return dfs(root, root.val)

        # def dfs(node, maxVal):
        #     if not node:
        #         return 0

        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res

        # return dfs(root, root.val)