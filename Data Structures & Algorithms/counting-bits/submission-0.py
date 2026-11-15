class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[] 
        for m in range(n+1):
            nmbr=0
            while m:
                m&=(m-1)
                nmbr+=1
            res.append(nmbr)
        return res 
            
