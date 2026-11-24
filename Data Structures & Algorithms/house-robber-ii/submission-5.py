class Solution:
    def rob(self, nums: List[int]) -> int:

        #bottom up space optimazation o(1)space   o(n)time
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(sub_nums):
            m = len(sub_nums)
            next1=0
            next2=0

            for i in range(m - 1, -1, -1):
                curr = max(sub_nums[i] +next2 , next1)
                next2 , next1 = next1 , curr

            return next1 
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1])) 


"""       #bottom up  o(n) space and time
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(sub_nums):
            m = len(sub_nums)
            dp = [0] * (m + 2)

            for i in range(m - 1, -1, -1):
                dp[i] = max(sub_nums[i] + dp[i + 2], dp[i + 1])

            return dp[0]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
"""

"""
        #memoazation o(n) space and time
        #we cant use the same memo for both calls (crete a rob linear helper fnct pr pass memo as key in recc function ) 
#helper fnct rob linear
    def rob(self, nums: List[int]) -> int:  
        if len(nums) == 1:
                return nums[0] 

        def rob_linear(nums):  
               
            memo={}
            def recc(i):  #pass memo as key
            #BASE CASES 
                if i >= len(nums): return 0
                if i in memo:
                    return memo[i]
                else: 
                    memo[i]=max( recc(i+2)+nums[i] , recc(i+1) ) 
                    return memo[i]
            return recc(0)
        return max(rob_linear(nums[1:]) , rob_linear(nums[:-1]))


"""
"""
#memo as key o(n) space and time
        if len(nums) == 1:
            return nums[0]
        def recc(i,sub_nums,memo):  #pass memo as key
            #BASE CASES 
            if i >= len(sub_nums): return 0
            if i in memo:
                return memo[i]
            else: 
                memo[i]=max( recc(i+2,sub_nums,memo) + sub_nums[i] , recc(i+1,sub_nums,memo) ) 
                return memo[i]

        return max(recc( 0 , nums[1:],{}) , recc(0, nums[:n-1],{}))
"""

"""
recurssion -->TLE   time O(2^N)  , space : o(n)
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