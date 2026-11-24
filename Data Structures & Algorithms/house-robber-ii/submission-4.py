class Solution:
 def rob(self, nums: List[int]) -> int:  

        #memoazation 
        n=len(nums)
        
        if n == 1:
            return nums[0]
        def recc(i,sub_nums,memo):
            #BASE CASES 
            if i >= len(sub_nums): return 0
            if i in memo:
                return memo[i]
            else: 
                memo[i]=max( recc(i+2,sub_nums,memo) + sub_nums[i] , recc(i+1,sub_nums,memo) ) 
                return memo[i]

        return max(recc( 0 , nums[1:],{}) , recc(0, nums[:n-1],{}))


"""
recurssion -->TLE
    def rob(self, nums: List[int]) -> int:  
        n=len(nums)
        if n == 1:
            return nums[0]
        def recc(i,sub_nums):
            #BASE CASES 
            if i >= len(sub_nums): return 0
            else: 

                return max( recc(i+2,sub_nums) + sub_nums[i] , recc(i+1,sub_nums) ) 

        return max(recc( 0 , nums[1:]) , recc(0, nums[:n-1]))

"""