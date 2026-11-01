"""
Store words in a trie and when searching, do a recursive dfs  when you hit a `.`, try every child branchand return `True` if any one of them finishes on a node marked as the end of a word.


Time complexity:  O(n) for addWord(),
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
                    if c==".":   
                        for child in curr.children.values():
                            if dfs(i+1,child):
                                return True
                        return False   #if no child is a match 
                    else:
                        if c not in curr.children:
                            return  False 
                        curr= curr.children[c]
                return curr.endofword 
            return dfs(0,self.root)

