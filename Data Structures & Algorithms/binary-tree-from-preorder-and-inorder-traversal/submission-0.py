# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """ Time and space complexity: o(n^2) 
        Recursion :the first value in the preorder is the root,values in the left of the root in the inorder list r going to be in root.left, every value in the right of this list will go to the right subtree """
        
        if not preorder or not inorder:
            return None 
        root_val=preorder[0]
        root=TreeNode(root_val)
       
        leftTreelength = inorder.index(root_val) 
        
        root.left= self.buildTree(preorder[1:leftTreelength+1], inorder[: leftTreelength])  #exclusive
         
        root.right=self.buildTree(preorder[leftTreelength+1:], inorder[leftTreelength+1:])
        return root 