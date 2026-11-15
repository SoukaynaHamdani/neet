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