class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        "intui: compare the len of the string - max frequent character and compare it against k "
        freq_map={}
        l=0
        r=0
        max_lenght=0
        for r in range(len(s)):
            freq_map[s[r]]=1+ freq_map.get( s[r], 0)
            while (r-l+1)-max(freq_map.values())>k :                
                freq_map[s[l]]-=1 
                l+=1
            max_lenght=max( max_lenght,r-l+1)
        return max_lenght
