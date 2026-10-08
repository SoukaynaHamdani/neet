class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        res=[]
        for num in nums:
         seen.add(num)
        for n in seen:
            if (n-1) not in seen:  
                count=1 
                while n+1 in seen:     #while not if
                    count+=1 
                    n+=1
                    res.append(count)
                    
        return max(res,default=1)