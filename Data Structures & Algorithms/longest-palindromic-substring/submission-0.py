class Solution:
    def longestPalindrome(self, s: str) -> str:
        best=""
        l=0
        r=0
        def helper(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        if len(s[l+1:r])>len(best):
                best=s[l:r]
        for i in range(len(s)):        
            l+=1
            r+=1
            best=helper(l,r)
            best=helper(l,r+1)
        return best