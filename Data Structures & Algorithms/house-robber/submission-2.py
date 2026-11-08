class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursive
        n=len(nums)
        def helper(i):  #helper= max money 
            if i==0:
                return nums[0]
            if i==1: 
                return max(nums[0], nums[1])   

            return max(helper(i-2)+ nums[i] , helper(i-1))    

        return helper(n-1)