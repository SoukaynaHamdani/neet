# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

            """O(N) time 
               O(H) space(recursive call stack)  worst case (tree height unbalnced H=N)  Best case log N
               swap -->Recursion (inver happens from root to leaves)  or Recursion-->swap (leaves to root) """
            if not root:
                return 
            root.right , root.left =  root.left, root.right
            self.invertTree(root.left) 
            self.invertTree(root.right)  
             
            return root 
 