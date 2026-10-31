# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            """sort with helper fnct inorder_dfs  retur k-1 cuz it is 1-indexed  
            time and space o(n)
            """
            res=[]
            if not root:
                return None  
            
            def inodfs(node) :
                if not node: return  #base case else infinit recursion 
                inodfs(node.left)
                res.append(node.val )
                inodfs(node.right)
 
            inodfs(root)
            return res[k - 1]
"""
        #iterative approach:
        #o(H)space(stack)  O(H + k) time wost casen
            n=0
            stack=[]
            curr=root
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr= curr.left
                curr=stack.pop()
                n+=1
                if n==K:
                    return curr.val
                curr=curr.right
"""

