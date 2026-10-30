# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Time:(O(h)  Space: O(h) recursion Call Stack.
        For a balanced BST, both are O( log n)  else O(n)"""

        if root.val > p.val and root.val > q.val: 
                return self.lowestCommonAncestor(root.left,p,q)

        elif root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right,p,q)

        else:
                return root 


