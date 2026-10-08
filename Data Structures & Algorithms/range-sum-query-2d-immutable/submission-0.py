class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
         
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                 
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix[r][c + 1]  
                    + self.prefix[r + 1][c]  
                    - self.prefix[r][c]      
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
         
        return (
            self.prefix[r2][c2] 
            - self.prefix[r1 - 1][c2]     
            - self.prefix[r2][c1 - 1]      
            + self.prefix[r1 - 1][c1 - 1]  
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)