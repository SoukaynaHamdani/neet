"""
Return positions in both the Atlantic and Pacific sets
We work in reverse from the oceans to the cells. Run DFS on each column in the first row, passing the Pacific set and setting prevHeight to the current position's value: dfs(0, c, pac, heights[0][c]). Repeat for the last row using the Atlantic set.

Do the same using another loop for every row in the first and last columns.

Finally, iterate through every position in the grid; if (r, c) belongs to both sets, append it to the result.

O(n*m)
space sets store nmbr of elemets (N*M) also the call stack
and time , we visit each position once since we have visited so we visit o(m*n) in bfs and in the nested loop 
"""


class Solution:
    def pacificAtlantic(self, heights):

        rows, cols = len(heights), len(heights[0])
        paci = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            #elimination 
            if (r < 0 or c < 0 or 
                r == rows or c == cols or 
                (r, c) in visited or 
                heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            
             
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col, visited, heights[r][c])

        
        for c in range(cols): #up and down 
            dfs(0, c, paci, heights[0][c])           # Pacific  
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # Atlantic  

        # 4. right and left
        for r in range(rows):
            dfs(r, 0, paci, heights[r][0])           # Pacific 
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # Atlantic  

        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in paci and (r, c) in atl:
                    res.append([r, c])

        return res