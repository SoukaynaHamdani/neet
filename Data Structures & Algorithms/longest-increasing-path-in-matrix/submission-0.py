class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS= len(matrix),len(matrix[0])
        dp={}   #(r,c)--> LIP 

        def dfs(r,c,prevVal):
            #elimination 
            if (r< 0 or r==ROWS or
                c<0 or c==COLS  or
                matrix[r][c]<=prevVal):
                    return 0 

            if (r,c) in dp:
                return dp[(r,c)]

            res=1 
            directions=[(1,0),(0,1), (-1,0),(0,-1)]
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                res=max(res, 1+ dfs(row,col,matrix[r][c]))
            dp[(r,c)]=res 
            return res 
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)   #without return 

        return max(dp.values())