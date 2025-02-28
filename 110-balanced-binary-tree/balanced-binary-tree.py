# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root: return 0
            leftheight, rightheight = height(root.left), height(root.right)
            return 1+ max(leftheight, rightheight)
            # if leftheight<0 or rightheight<0 or abs(leftheight-rightheight)>1: return -1
            # return max(leftheight, rightheight)+1

        
        if not root: return True
        if abs(height(root.left)- height(root.right))>1: return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)