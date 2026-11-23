class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        target = (Rows - 1, Cols - 1)
        
        def recc(r, c, curr_sum):
            if r < 0 or r == Rows or c < 0 or c == Cols:
                return float("inf")
            if (r, c) == target:
                return curr_sum + grid[r][c]

            return min(
                recc(r + 1, c, curr_sum + grid[r][c]),
                recc(r, c + 1, curr_sum + grid[r][c])
            )
             
        return recc(0, 0, 0)