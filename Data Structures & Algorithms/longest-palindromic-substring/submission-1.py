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
        
        for i in range(len(s)):        
            odd=helper(i, i)
            even=helper(i, i + 1)
            if len(odd)>len(best):
                best=odd
            if len(even)>len(best):
                best=even

        return best