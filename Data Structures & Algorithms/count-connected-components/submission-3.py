class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """o(V+E) time and space  adjacency list + visited set + dfs to add all nei to visited. for each node in range of n if it is not a visited its a nwe graph nbr+=1 and run dfs to add all its neighbors to visited"""
        mapp = defaultdict(list)
        for u, v in edges:
            mapp[u].append(v)
            mapp[v].append(u)
            
        visited = set()
        nbr = 0  

        def dfs(node):
            visited.add(node)
            for nei in mapp[node]:
                if nei not in visited:
                    dfs(nei)

         
        for i in range(n):
            if i not in visited:
                nbr += 1        
                dfs(i) 
 
        return nbr       





"""class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
         union find algorithm
        Start by treating every node as its own independent island (res = n ). For every edge, if the two nodes n1 ,n2 are on separate islands, bridge them together (union (find super parent then do union based on rank )) and reduce your total component count by one 

        Time complexity: O(V+(E∗α(V)))
Space complexity: O(V)
Where
V is the number of vertices and 
E is the number of edges in the graph. 
α() Inverse Ackermann) for amortized complexity. 

        par= [i for i in range(n)]
        rank=[1]*n

        def find(n1):  #find the parent 
            res=n1 
            while res!=par[res]:# we stope once a node is parent of itself 
                par[res]=par[par[res]] #if it exists , path compression 
                res=par[res]
            return res #the super parent

        def union(n1,n2):
                p1,p2=find(n1),find(n2)

                if p1==p2:   #they have the same parent 
                    return 0  #we didnt do any union 
                
                if rank[p2]>rank[p1]:
                    par[p1]=p2  #parent of p1 is p2
                    rank[p2]+=1+rank[p1]
                else: 
                    par[p2]=p1   
                    rank[p1]+=1+rank[p2]
                return 1 
        res=n
        for n1,n2 in edges:
            res-= union(n1,n2)
        return res 


"""               