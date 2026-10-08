class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for n in seen:
            if (n-1) not in seen:  
                count=1 
                while n+1 in seen:     #while not if
                    count+=1 
                    n+=1
                longest = max(longest, count)
                    
        return longest