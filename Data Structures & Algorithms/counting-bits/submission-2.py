class Solution:
    def countBits(self, n: int) -> List[int]:
            "dp o(n) space and time  dp[i]=1+dp[i-offset]"

            dp=[0]*(n+1)
            offset=1
            for i in range(1,n+1):
                if offset*2==i: #the most significant  bit 
                    offset=i
                dp[i]=1+dp[i-offset]
            return dp
    """
        res=[] 
        for m in range(n+1): #O(n)
            nmbr=0
            while m:  # O (log n) nbr of bits for each m is log n : 8 = 1000  has 4 bits 
                m&=(m-1)
                nmbr+=1
            res.append(nmbr)
        return res 
            
#time: O(n * log n), Space:O(n)
"""