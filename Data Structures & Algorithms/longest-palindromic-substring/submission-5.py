class Solution:
    def longestPalindrome(self, s: str) -> str:
        "intui :  use pinter at center and expand as char at left and right matches, repete same while loop for odd and even, use slicing just for the final result and keep track of resL and resR for o(n2)"
        l=0 
        r=0
        max_lenght=0
        for i in range(len(s)):
            #odd
            l,r=i,i
            while l>=0 and r<len(s) and s[l]== s[r]:
                if (r-l+1)>max_lenght: 
                    max_lenght=r-l+1
                    resL,resR =l ,r 
                l-=1
                r+=1 

            #even
            l,r=i,i+1
            while l>0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > max_lenght:
                    max_lenght=r-l+1
                    resL, resR = l,r 
                l-=1
                r+=1
        return s[resL :resR+1]
            

         