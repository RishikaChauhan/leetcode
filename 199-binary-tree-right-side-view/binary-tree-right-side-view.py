# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            r = None
            for i in range(qlen):
                val = q.popleft()
                if val:
                    r = val.val
                
                    q.append(val.left)
                    q.append(val.right)
            res.append(r)
        return res[:-1]
