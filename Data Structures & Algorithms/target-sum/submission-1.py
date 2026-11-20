class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: 
        dp=defaultdict(int)# map curr sum --> nmbr of ways to make up this sum 

        dp[0]=1 # to make a sume of 0 there is 1 way, not choosing any element 

        #loop trought each element 
        for num in nums :
            nextdp= defaultdict(int)
            for curr_sum , count in dp.items():
                nextdp[curr_sum + num]+=count 
                nextdp[curr_sum - num]+=count 
            dp=nextdp 
        return dp[target]