# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, node: Optional[TreeNode]) -> None:
        if not node: return 
        def dfs(root):
            head = root
            if not root: return None
            l = dfs(root.left)
            r = dfs(root.right)
            
            if root.left:
                temp = r
                root.right = l
                root.left = None
                while root.right: 
                    root = root.right
                    # root.left = None
                root.right = r
                # dfs(root.left)
            return head
        head = dfs(node)  
        return head