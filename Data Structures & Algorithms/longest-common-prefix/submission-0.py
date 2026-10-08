class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        IN STR 
        LONGET PREF
         
        """
        res=""
        for i in len(strs[0]):
            for s in strs:
                if i == len(s) or s[i]!=strs[0][i]:
                    return res 
                res+=strs[0][i]
            