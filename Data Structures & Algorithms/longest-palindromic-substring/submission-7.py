class Solution:
    def longestPalindrome(self, s: str) -> str:

        "intui :  use pinter at center and expand as char at left and right matches, one for loop (for each i it can form an odd or an even palindrom) so we repete same while loop for odd  l,r=i,i and even l,r=i,i+1 , use slicing just for the final results[resL :resR+1] (we keep track of resL and resR cuz l r will be out of bound cuz we appdate them after storing them for o(n2)"
        
        l=0 
        r=0
        max_lenght=0
        for i in range(len(s)):
            #odd
            l,r=i,i
            while l>=0 and r<len(s) and s[l]== s[r]:
                if (r-l+1)>max_lenght: 
                    max_lenght=r-l+1
                    resL=l                 #update just if (r-l+1)>max_lenght 
                l-=1
                r+=1 

            #even
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > max_lenght:
                    max_lenght=r-l+1
                    resL= l
                l-=1
                r+=1
        return s[resL :resL+max_lenght ]
            

         