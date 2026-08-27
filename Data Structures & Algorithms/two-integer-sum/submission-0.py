class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map= {} 
        for i in range(len(nums)):   
            diff= target - nums[i]
            if diff in map:
              return [map[diff], i] #ila 9lbtihum azkun galate 
            else:
                map[nums[i]]= i
