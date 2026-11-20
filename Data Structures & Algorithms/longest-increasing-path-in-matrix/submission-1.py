class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Plan: 2D Top-Down DP (DFS + Memoization)
        - Create a memoization map `dp` where key = (r, c) and value = length of
          the longest increasing path starting from cell (r, c).
        - Define `dfs(r, c, prevVal)`:
            * Base case (elimination): if (r, c) is out of bounds or
              matrix[r][c] <= prevVal, return 0.
            * Memoization : if (r, c) is already in `dp`, return dp[(r, c)].
            * Explore all directions (down, right, up, left), updating
              `res = max(res, 1 + dfs(row, col, matrix[r][c]))`.
            * Store `dp[(r, c)] = res` and return `res`.
        - Run `dfs(r, c, -1)` from every cell (r, c) in the grid (since  values are >= 0, -1 guarantees the starting cell is always valid).
        - Return `max(dp.values())` 

        Time Complexity:  O(m * n)  
        Space Complexity: O(m * n)  
        """

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