# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left 
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root
        
        
        
        
        
        if not root: return None
        if key== root.val:
            if not root.left and root.right: return root.right
            if not root.right and root.left: return root.left
            curr = root.right
            while curr and curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        elif key>root.val:
            self.deleteNode(root.right, key)
        else: self.deleteNode(root.left, key)
        return root
        