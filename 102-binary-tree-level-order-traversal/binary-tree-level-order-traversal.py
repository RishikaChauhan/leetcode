# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                val = q.popleft()
                if val:
                    level.append(val.val)
                    q.append(val.left)
                    q.append(val.right)
            res.append(level)
        return res[:-1]