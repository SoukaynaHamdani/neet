class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      l=0
      r=1
      for r in range(1,len(nums)):
        if nums[l]!=nums[r]:
            l+=1
            nums[l]=nums[r]
      return l+1 #nmber of unique elm 