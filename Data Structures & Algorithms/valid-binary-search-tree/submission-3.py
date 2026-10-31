# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            """ 
            time o(n)  valid visit each node 
            space O(h)   o(logn) if balanced 
            Every node in a BST lives between a lower and upper bound; moving left we update (Right Bound to be node.val), and moving right (Left Bound to node.val).
            """

            def valid(node ,left_bound, right_bound):
                if not node:  #base case
                    return True 
                if (left_bound< node.val<right_bound): 
                    return (valid(node.left,left_bound, node.val) and (valid(node.right, node.val,right_bound)))
                else:
                    return False
            return valid(root,float("-inf"), float(" inf")) 