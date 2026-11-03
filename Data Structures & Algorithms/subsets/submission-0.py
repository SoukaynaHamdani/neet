class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        sol=[]
        def backtrack(i):
            #base case:
            if i ==len(nums):
                res.append(sol[:])
                return
            
            #dont pick 
            backtrack(i+1)

            #pick 
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res 