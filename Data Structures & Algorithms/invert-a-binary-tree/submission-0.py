# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return 
            Rev_right=self.invertTree(root.right)   
            Rev_left=self.invertTree(root.left) 
            
            root.right , root.left =  Rev_left, Rev_right 
            return root 
 