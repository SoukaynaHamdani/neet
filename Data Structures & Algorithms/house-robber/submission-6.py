class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up dp- constant space 
        #o(n) time  o(1) space 

        n=len(nums) 
        #base case 
        if n == 1:  #one house 
            return nums[0]

        prev=nums[0]    #dp[i-2]

        curr=max(nums[0],nums[1])     #dp[i-1]
         
        for i in range(2,n):  #from index 2 to index n-1 the last index 
            prev,curr=curr, max(prev+nums[i], curr)

        return curr