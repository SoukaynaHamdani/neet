class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        target = (Rows - 1, Cols - 1)
        dp=[[float("inf")]* (Cols+1) for _ in range(Rows+1)]

        for r in range(Rows-1, -1,-1):
            for c in range(Cols-1,-1,-1): 
                if (r, c) == target:
                    dp[r][c] = grid[r][c]
                else : 
                    dp[r][c]= grid[r][c] + min(
                    dp[r + 1] [c],
                    dp[r] [c+1]
                    )

        return dp[0][0]
                

"""
        Rows = len(grid)
        Cols = len(grid[0])
        target = (Rows - 1, Cols - 1)
        memo={}   # r,c --> curr_sum 
        
        def recc(r, c):
        
            if r < 0 or r == Rows or c < 0 or c == Cols:
                return float("inf")
            if (r, c) == target:
                return grid[r][c]
            if (r,c) in memo: 
                return memo[(r,c)]

            memo[(r,c)]= grid[r][c] + min(
                recc(r + 1, c),
                recc(r, c + 1)
            )
            return memo[(r,c)]
        return recc(0,0)              
"""