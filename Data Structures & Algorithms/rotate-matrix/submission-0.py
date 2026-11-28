class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #Transpose(right)+ Reverse
        n=len(matrix)
        for r in range(n-1):    # i=0--> n-2 cuz we need to traspose  the right half the left will be automatic taken care of 
            for c in range(r+1, n):    #j= i+1 --> n-1 last col 
                matrix[r][c],matrix[c][r]=matrix[c][r], matrix[r][c]
        
        for row in matrix: 
            row.reverse() 
"""
       #brute force o(n^2 )
        n=len(matrix)
        ans=[[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n): 
                ans[j][n-1-i]=matrix[i][j]
        return ans
"""