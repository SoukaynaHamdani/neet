class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ we need to be greedy pushing the goal near 0 as we can 
        o(n) time , o(1) space 
        """

        goal=len(nums)-1
        for i in range(len(nums)-1 ,-1 ,-1):
            if i+nums[i]>=goal:
                goal= i
        return True if goal==0 else False
