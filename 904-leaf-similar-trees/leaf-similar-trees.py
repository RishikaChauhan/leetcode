# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def leaf1(root):
            if not root:
                return None
            if not root.left and not root.right:
                l1.append(root.val)
            leaf1(root.left)
            leaf1(root.right)
            
        def leaf2(root):
            if not root:
                return None
            if not root.left and not root.right:
                l2.append(root.val)
            leaf2(root.left)
            leaf2(root.right)
        
        leaf1(root1)
        leaf2(root2)
        print(l1)            
        print(l2)

        return l1==l2