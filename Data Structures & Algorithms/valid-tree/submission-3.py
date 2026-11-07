class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ undirected acyclic connected graph
        Edge Count Check:  number of edges equals the number of nodes-1  (n - 1 == len(edges)).

Undirected Graph: Build the adjacency list in both directions (u to v and v to u).

Track the previous node during DFS to avoid false cycle detection when going back to the parent + visted set to detect cycles.

Connectivity Check: Ensure all nodes are visited and connected  if n == len(visited)  
Time and space: O(V + E)"""
        if not n:  #empty graph is a valid tree 
            return True 
        mapp=defaultdict(list)
        for u,v in edges:  # adjacency list map: o(E) time/ O(V + E) space 
            mapp[u].append(v)
            mapp[v].append(u) #undirected 
  
        if n-1!=len(edges) :  #E = V - 1
            return False 
        visited= set() 

        def dfs(node, prev):  # detect cycles  O(V + E) time and O(V) space 
            #cycle detected  elimination 
            if node in visited:
                return False 

            visited.add(node)

            for nei in mapp[node]:
                if nei==prev:
                    continue
                if not dfs(nei,node):
                    return  False 
            return True 
        return dfs(0, -1) and n==len(visited)  #connected
        
