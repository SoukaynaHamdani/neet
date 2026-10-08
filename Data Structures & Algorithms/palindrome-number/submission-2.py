class Solution:
    def isPalindrome(self, x: int) -> bool:
        strs=str(x)
        l=0
        r = len(strs)-1
        #if strs[l]==strs[r]:return True
        while l<r:
            if strs[l]!=strs[r]:
                return False
            else:
                l+=1
                r-=1
        return True 
            
