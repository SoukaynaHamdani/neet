class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r == Rows or
                c < 0 or c == Cols or
                (r, c) in visited or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)

        islands = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands
        
        
        
"""   
     from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(start_r: int, start_c: int) -> None:
            queue = deque([(start_r, start_c)])
            visited.add((start_r, start_c))  # Mark visited immediately on push!

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    
                    #valid not elimination  
                    if (
                        0 <= row < Rows and
                        0 <= col < Cols and
                        (row, col) not in visited and
                        grid[row][col] == "1"
                    ):
                        visited.add((row, col))
                        queue.append((row, col))

        islands = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
"""