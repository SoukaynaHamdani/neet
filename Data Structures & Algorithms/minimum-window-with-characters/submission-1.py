class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        intu: Maintain two frequency maps (countT and window for s). for each char that is both in s and t if their freq is equal : have += 1, 
        while have == need  update resLen and res. Then window[s[l]]-=1 then if window[s[l]] < countT[s[l]] have -=1 , then start removing elements from left  
        """
        if t=="": return""
        l=0
        r=0 
        countT={}
        window={}
        resLen= float("infinity")
        res= [0,0]
        have=0
        for ch in t:
            countT[ch]=1+countT.get(ch,0)
        need=len(countT)
        for r in range(len(s)):
                window[s[r]]=1+window.get(s[r],0)
                if s[r] in countT and window[s[r]] == countT[s[r]]:
                 have+=1
                while have==need:
                    #shrink 
                    if (r-l+1)<resLen: 
                        resLen=(r-l+1)
                        res=[l,r]
                    
                    window[s[l]]-=1
                    if s[l] in countT and window[s[l]]<countT[s[l]]:
                        have -=1 
                    l+=1    
        l,r=res     
                        
        return s[l:r+1] if resLen!= float("infinity") else ""
                    
