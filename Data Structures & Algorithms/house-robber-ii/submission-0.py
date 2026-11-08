class Solution:
    def rob(self, nums: List[int]) -> int:
        """ DP Bottom-Up (Tabulation)
        Time: O(n)
        Space: O(n) 
    run dp 2 times, excluding the first house and then exluding the last house and return the max of the 2 using slicing and helper fnct""" 

        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def rob_linear(houses):
            k=len(houses)
            dp=[0]*k
            dp[0]=houses[0]
            dp[1]=max(houses[0],houses[1])

            for i in range(2,k):
                dp[i]= max(dp[i-2]+houses[i], dp[i-1])
            return dp[k-1]

        return max(rob_linear(nums[1:]),rob_linear(nums[:n-1]) )
