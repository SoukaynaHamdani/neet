class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
    
        if len(nums)==1 and nums[0]==target:
                return 0
        elif len(nums)==2:
             if nums[0]==target:
                return 0
             elif nums[1]==target:
                return 1
        else:
                while left<right:
                    
                    mid=(left+right)//2
                    if nums[mid]==target:
                        return mid 
                    elif nums[mid]>target and  nums[mid]>nums[left]:
                        left+=1
                    else:
                        right=mid 
        return -1

