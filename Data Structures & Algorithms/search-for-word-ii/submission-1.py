"""complexity:  
O(R*C*4*(3^t-1)+s)
Space complexity:  O(s)
Where  R is the number of rows, 
C is the number of columns, 
t is the maximum length of any word in the array words and 
s is the sum of the lengths of all the words."""
class TrieNode: 
    def __init__(self):
        self.children= {}
        self.endofword=False 
    def addword(self,word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endofword=True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
         
        Rows=len(board)
        Cols=len(board[0])
        visited =set()
        res=set()

        
        #fill the trie
        root=TrieNode()
        for word in words:
            root.addword(word)

        #recursive dfs +backtracking 
        def dfs(r,c, node, word):
    

            #elimination 
            if (r<0 or c <0 or
                r>=Rows or c>=Cols or 
                (r,c) in visited or 
                board[r][c] not in node.children):
                    return False 
            
            #normal case backtracking (dfs 4 direction inside )
            visited.add((r,c))

            node=node.children[board[r][c]]   #gives the node of the element we are at in the grid 
            word+=board[r][c]

            if node.endofword:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))   #we remove when moving to the next word in words 

            
        for r in range(Rows):
                for c in range(Cols):
                    dfs(r,c,root,"")
        return list(res)
