class Solution:
    def getSum(self, a: int, b: int) -> int:
        #return sum([a,b])
        #return int(math.log(math.exp(a)*math.exp(b)))
        while b>0:
            a, b = a ^ b, (a & b) << 1
        return a