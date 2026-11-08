class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up - tabulation- removes recursion so no helper-->iterative for loop 
        #o(n) space and time 

        n=len(nums) 
        #base case 
        if n == 1:  #one house 
            return nums[0]

        dp=[0]*n
        dp[0]=nums[0]

        dp[1]=max(nums[0],nums[1])
         
        for i in range(2,n):  #from index 2 to index n-1 the last index 
            dp[i]=max(dp[i-2]+nums[i], dp[i-1])

        return dp[n-1]