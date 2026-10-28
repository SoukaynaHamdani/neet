# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True 
            if not p or not q:
                return False
            else:
                if p and q:
                    if p.val == q.val: 
                        same_r=self.isSameTree(p.right, q.right) 
                        same_l=self.isSameTree(p.left,q.left) 
                        return  same_r and same_l
            return False
