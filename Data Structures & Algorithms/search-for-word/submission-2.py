
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ dfs on each cell, for each search remember visited cells(path), hen uses DFS  with backtracking across all four directions to verify if the rest of the word can be spelled out.   and remove cur visited cell right before you return from dfs;

        time  O(N * M * 4^L)
        Space Complexity: O(L)L is the length of the word)"""
        Rows=len(board)
        Cols=len(board[0])
        path=set()

        def dfs(r,c,i):

            if i==len(word):
                return True 

            if (r<0 or c<0 or
            r>=Rows or c>=Cols or
            word[i]!=board[r][c]  or
            (r,c) in path) :
                return False 
            #else
            path.add((r,c))  # add the position  
            res=(dfs(r+1,c,i+1)or
                dfs(r-1,c,i+1)or
                dfs(r,c+1,i+1)or
                dfs(r,c-1,i+1))
            path.remove((r,c)) 
            return res 
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r,c,0): return True 
        return False
