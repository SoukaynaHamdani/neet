class Solution:
    #DP- bottom up-->Tabulation. LST-->dp
    #start looping i from the end of the arry and j from i+1,  if nums[i]<nums[j] --> LIS[i]=max(LIS[i], 1+ LIS[j])
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)

        for i in range(len(nums)-1 , -1 ,- 1): 
            for j in range (i+1,len(nums)): 
                if nums[i]<nums[j]: 
                    LIS[i]=max(LIS[i], 1+ LIS[j])
        return max(LIS)
    
#  time o(n^2)
#space o(n)
"""
# Top-Down DP (Memoization)
memo = {}
def dfs(i):
    if i in memo:
        return memo[i]
    res = 1
    for j in range(i + 1, len(nums)):
        if nums[i] < nums[j]:
            res = max(res, 1 + dfs(j))
    memo[i] = res
    return res

    Top-Down (dfs): Starts at i = 0, calls dfs(j) for larger indices, and caches answers in memo[i] on the way back.

  (Bottom-Up Tabulation): Eliminates recursion by filling LIS[i] from right to left (len(nums) - 1 down to 0), guaranteeing that every LIS[j] (j > i) is already computed before LIS[i] needs it.
    """