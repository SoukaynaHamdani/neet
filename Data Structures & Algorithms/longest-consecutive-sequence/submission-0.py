class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        count=0
        for num in nums:
         seen.add(num)
        star=min(seen)
        for i in range(len(nums)):
            if star in seen:
                count+=1
                star+=1
        return count