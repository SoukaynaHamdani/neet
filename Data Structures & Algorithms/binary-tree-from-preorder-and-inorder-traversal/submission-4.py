# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """ hashmap +dfs helper fonction with Recursion :the first value in the preorder is the root,values  in the left of the root in the inorder list r going to be in root.left, every value in the right of this list will go to the right subtree
      o(n) space and time """

        indices={val : indx  for indx , val in enumerate(inorder)}

        self.preo_indx=0
        def dfs(l,r):
                if l > r: #base case 
                        return None
                root_val=preorder[self.preo_indx]
                root=TreeNode(root_val)
                self.preo_indx+=1      #self 
                mid =indices[root_val]
                root.left= dfs(l,mid-1)
                root.right=dfs(mid+1,r)
                return root
        return dfs (0,len(inorder) - 1)