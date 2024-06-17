# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(a, b):
            if not a and not b:
                return True
            if a and not b: return False
            if b and not a: return False
            if b and a and b.val != a.val: return False
            return ismirror(a.left, b.right) and ismirror(a.right, b.left)
        
        if not root: return True
        return ismirror(root.left, root.right)