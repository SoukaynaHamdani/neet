class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapp=defaultdict(list)

        for u,v in edges:
            mapp[u].append(v)
        
        e=len(edges)
        if n-1!=e :
            return False 
        visited= set()
        def dfs(node): 
            if node in visited:
                return False 
            for nei in mapp[node]:
                if not dfs(nei):
                    return  False 
            visited.remove(node)
        return True 
        
