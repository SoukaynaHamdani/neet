class Solution:
    def rob(self, nums: List[int]) -> int:
        """ DP Bottom-Up (constant space)
        Time: O(n)
        Space: O(1) 
    run dp 2 times, excluding the first house and then exluding the last house and return the max of the 2 using slicing and helper fnct""" 

        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def rob_linear(houses):
            k=len(houses)
            prev=houses[0]
            curr=max(houses[0],houses[1])

            for i in range(2,k):
               prev ,curr=curr,  max(prev+houses[i], curr)
            return curr

        return max(rob_linear(nums[1:]),rob_linear(nums[:n-1]) )
