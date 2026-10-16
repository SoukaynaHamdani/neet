class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        seen=set()
        max_lenght=0 
        for char in s:
            while char in seen:   
                seen.remove(s[l])
                l+=1
             
            max_lenght=max(max_lenght,r-l+1)
            seen.add(char)
            r+=1
        return max_lenght
            
             
                
        
