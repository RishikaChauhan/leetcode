# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, z= [], 1
        q = [root]
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            res.append(level[::z])
            z*=-1
        return res

