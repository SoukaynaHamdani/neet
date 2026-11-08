class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down dp - memozation 
        #o(n) space and time 

        n=len(nums) 
        #base cases 
        if n == 1:  #one house 
            return nums[0]
        memo={0:nums[0] , 1:max(nums[0],nums[1])}
         
        def helper(i): 
            if i in memo:
                return memo[i]
            memo[i]=max(helper(i-2)+nums[i], helper(i-1))
            return memo[i]
        return helper(n-1)