class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums)-1
        while l<= r: 
            if nums[l]== target:
                return l 
            mid = (l+r )//2  
            if nums[mid]>=nums[l]:
                if nums[l]<= target < nums[mid]: 
                    l=mid+1
                else: 
                    r=mid-1
            else: 
                if nums[mid] <target <=nums[r]:
                    r=mid-1
                else :
                    l=mid+1
        return -1

