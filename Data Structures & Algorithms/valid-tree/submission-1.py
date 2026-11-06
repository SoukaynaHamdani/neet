class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ undirected  acyclique connected graph """
        if not n:  #empty graph is a valid tree 
            return True 
        mapp=defaultdict(list)

        for u,v in edges:
            mapp[u].append(v)
            mapp[v].append(u) #undirected 

        e=len(edges)
        if n-1!=e :
            return False 
        visited= set()

        def dfs(node, prev):  #to detect cycles 
            #cycle detected 
            if node in visited:
                return False 

            visited.add(node)

            for nei in mapp[node]:
                if nei==prev:
                    continue
                if not dfs(nei,node):
                    return  False 
            return True 
            visited.remove(node)
        return dfs(0, -1) and n==len(visited)  #connected
        
