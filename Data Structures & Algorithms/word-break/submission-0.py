class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res=False
        tem=""
        for word in wordDict:
            for ch in s: 
                    if ch in word:
                        continue 
                        tem+=ch
                    else:
                        z=len(tem) 
                        s=s[z:]  
                        break
        return True 
                              
