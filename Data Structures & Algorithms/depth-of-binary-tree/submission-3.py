# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
                #Reccur 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
                #o(N) time, o(H)space (H best case(balanced)= logn  worst = n) 
                if not root:
                    return 0 
                return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
