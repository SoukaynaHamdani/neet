class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
         

        def dfs(r: int, c: int) -> int:
            # Base case: out of bounds, water (0), or already visited
            if (
                r < 0 or r == Rows or
                c < 0 or c == Cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            area = 1  # Count current cell

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                area += dfs(row, col)

            return area

        max_res = 0
        for r in range(Rows):
            for c in range(Cols):
                max_res = max(max_res, dfs(r, c))

        return max_res