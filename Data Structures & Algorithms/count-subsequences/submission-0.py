class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cach={} #indecies (i,j)--> longest way starting at these indecies 

        #base case 
         
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0 
            if (i,j) in cach: 
                return cach[(i,j)]
         
            if s[i]== t[j]:
                cach[(i,j)]=dfs(i+1,j+1)+ dfs(i+1,j)

            else:
                cach[(i,j)]= dfs(i+1,j)
            return cach[(i,j)]
        return dfs(0,0)