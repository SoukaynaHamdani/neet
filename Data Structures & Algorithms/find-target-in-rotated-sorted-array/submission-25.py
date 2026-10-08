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
                    l+=1 
                else: 
                    r-=1
            else: 
                if nums[mid] <target <=nums[r]:
                    r-=1
                else :
                    l+=1 
        return -1

