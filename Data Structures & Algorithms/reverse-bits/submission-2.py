class Solution:
    def reverseBits(self, n: int) -> int:

        """we start res= 0 , for i in rang 32 we shift the result to left , if the last element in n is 1 we add it to res and then we right shift our n to process the next bit
        o(1) space and time """
        res=0
        for i in range(32):
            res=res<<1
            if (n%2==1):     # or ( n&1) ==1):  or #res = res | (n & 1)   
                res+=1
            n=n>>1
        return res 

"""
follow up : if this fnct is called many times how to optimize it 
class Solution:
    def reverseBits(self, n: int) -> int:
        n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)
        n = ((n & 0xff00ff00) >> 8)  | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4)  | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2)  | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1)  | ((n & 0x55555555) << 1)
        return n
"""