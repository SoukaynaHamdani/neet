"""Time complexity:  O(n) for addWord(),
O(n) for search().
Space complexity: O(t+m)
m is the length of the string and 
t is the total number of TrieNodes created in the Trie."""

class TrieNode: 
    def __init__(self) :
        self.children={}
        self.endofword= False 

class WordDictionary:
        def __init__(self):
            self.root= TrieNode()
        def addWord(self, word):
            curr=self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr= curr.children[c]
            curr.endofword=True

        def search(self,word):

            def dfs(j,root): #root
                curr=root
                for i in range(j,len(word)):
                    c=word[i]
                    if c==".":   #skip it 
                        for child in curr.children.values():
                            if dfs(i+1,child):
                                return True

                    else:
                        if c not in curr.children:
                            return  False 
                        curr= curr.children[c]
                return curr.endofword 
            return dfs(0,self.root)

