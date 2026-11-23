class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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