class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[] 
        for m in range(n+1): #O(n)
            nmbr=0
            while m:  # O (log n) nbr of bits for each m is log n : 8 = 1000  has 4 bits 
                m&=(m-1)
                nmbr+=1
            res.append(nmbr)
        return res 
            
#time: O(n * log n), Space:O(1)
