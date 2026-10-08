class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l] <= nums[mid]:#left sorted  <= !!!
                if nums[l] <= target < nums[mid]:  
                    r=mid-1 
                else:
                    l=mid+1
            else:
                   
                if nums[mid] < target <= nums[r]: #right sorted portion
                    l = mid + 1  # نمشيو لليمين
                else:
                    r = mid - 1  # نمشيو لليسار
                
        return -1
                    

