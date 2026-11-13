class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """O(n) time , o(1)space """
        " Dp :res=max(nums), keep track of the min and max and the number we are at n  if n=0 reset both to 1 then continue"

        res=max(nums)   #[-1] max is -1 not 0 so we cant initialise res to 0 
        currMin ,currMax=1,1
        for n in nums: 
            if n==0:
                currMin ,currMax=1,1
                continue
 
            temp=currMax
            currMax= max(currMax*n,currMin*n,n)  #[-1,8] max is n=8
            currMin= min(currMin*n,temp*n,n)
            res= max(currMax,res)
        return res 
