class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums)  #not []
        prefex=1 
        for i in range(len(nums)):
            res[i]=prefex
            prefex*=nums[i]
        sufex=1 
        for i in range(len(nums)-1,-1,-1):
            res[i]*=sufex
            sufex*=nums[i]
        return res 
        