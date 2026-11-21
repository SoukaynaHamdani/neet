class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # O(N * L + K)  N=nmbr of words , L averagge word length , kk average nbr of unique caracters 
        # (Space Complexity): O(K + E) to store adj , visited , recursion stack 
        #build the adjacency dictionary , mapping each caracter to its neighbors 
        adj={c:set() for word in words for c in word}

        for i in range(len(words)-1):
            w1,w2= words[i], words[i+1]
            minLen= min(len(w1), len(w2))
            
            #invalide case 
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                    return ""

            #connect the edges
            for j in range(minLen): 
                if w1[j]!=w2[j]: 
                    adj[w1[j]].add(w2[j])
                    break   # we break after the first mismatch

        visited={}     #false means visited this node and all its neigborhs ,  true means we visited this node and it is in the current path so we detected a  cycle 
        res=[] 
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c]=True 
            for nei in adj[c]:
                if dfs(nei):
                    return True   #we found a cycle 
            
            #once the loop visits all  neigbors we go back from the call stack , we append the last neighbor to the res and mark its  visited[c]=False , and go to its parent where we will do the same cuz it has already visited all its neigborhs      
            visited[c]=False
            res.append(c)

        #we ran dfs on all nodes of the graph if we have disconected components we need to process them and to check for cycles 
        for c in adj:
            if dfs(c):
                return ""  #we found a cycle 

        #we return the reverse of res, cuz we performed post order traversal we add a node to res after visiting and adding all its neigborhs.
        ans=[]
        while res:
            ans.append(res.pop())
        return "".join(ans)      # or res.reverse()

