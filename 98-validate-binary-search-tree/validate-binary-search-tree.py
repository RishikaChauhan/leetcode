# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(left, node,right):
            if not node: return True
            if left<node.val<right:
                return valid(left, node.left, node.val) and valid(node.val, node.right, right)
            else:return False
        return valid(float("-inf"), root, float("inf"))
        