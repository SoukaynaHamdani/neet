"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Time Complexity O(V + E)
         Space O(V) """
        oldtoNew={}

        def recursivedfs(node):
            if node in  oldtoNew:
                return oldtoNew[node]    #if it is alredy cloned we return the clone 

            copy = Node(node.val)
            oldtoNew[node]=copy
            for nei_node in node.neighbors:
                #run dfs on the neighboor  and add them to the copy 
                    copy.neighbors.append(recursivedfs(nei_node))
            return copy 
        
        return recursivedfs(node) if node else None
