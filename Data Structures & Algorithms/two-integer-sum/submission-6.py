class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for num, indx in enumerate(nums):
            hmap[num]=indx 
        
        for i in range(len(nums)):
            diff= target - nums[i]
            if diff in hmap and hmap[diff] != i:
                return [hmap[diff],i]
            else:
                hmap[nums[i]]=i