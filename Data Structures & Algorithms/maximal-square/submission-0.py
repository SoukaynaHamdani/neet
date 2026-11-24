class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:

        #DP- TABUlation -  bottom up 
        Rows= len(grid) 
        Cols=len(grid[0]) 
        dp=[[0]* (Cols+1) for _ in range(Rows+1)]

        for r in range(Rows -1 ,-1,-1): 
            for c in range(Cols-1,-1,- 1): 
             
                if grid[r][c]=="0":
                     dp[r][c]=0 
                else: 
                    dp[r][c]= 1+ min(dp[r+1][c] , dp[r][c+1] , dp[r+1] [c+1])

  
        maxx=0 
        for r in range(Rows):
            for c in range(Cols): 
                maxx=max(maxx, dp[r][c]) 
        return maxx *maxx




"""DP - TOP DOWN MEMOAZTION  
        Rows= len(grid) 
        Cols=len(grid[0]) 
        memo={}

        def recc(r,c): 
            
            if  (r<0 or r==Rows or 
                c<0 or c==Cols or 
                grid[r][c]=="0"):
                    return 0 
            if (r,c) in memo: 
                return memo[(r,c)]

            memo[(r,c)]= 1+ min(recc(r+1,c) , recc(r,c+1) , recc(r+1,c+1))

            return memo[(r,c)]

        maxx=0 
        for r in range(Rows):
            for c in range(Cols): 
                maxx=max(maxx,recc(r,c)) 
        return maxx *maxx
"""
