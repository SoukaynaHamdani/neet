# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

            """ BFS iterative, add to the lev list the nodes in that level with for loop (nmb of nodes in each level = lenght of my queue pefore poping) 
            o(N) space and time """
            from collections import deque
            q=deque()
            if not root:
                return [] 
            q.append(root) 
            res=[]
            
            while q:
                lenght=len(q)             
                lev=[]  
                for i in range(lenght):
                    node=q.popleft()  
                    if node:
                        lev.append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                if level:
                    res.append(lev)
            return res 
