# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issametree(p, q):
            if (not p and not q):
                return True
            elif p and q and p.val== q.val:
                return issametree(p.left, q.left) and issametree(p.right, q.right)
            else: return False
        if not root and subRoot: return False
        if root:
            if issametree(root, subRoot): return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot): return True
        return False

