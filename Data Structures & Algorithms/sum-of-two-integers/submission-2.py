class Solution:
    def getSum(self, a: int, b: int) -> int:
        #return sum([a,b])
        #return int(math.log(math.exp(a)*math.exp(b)))

#we creat a mask 32 ones to be bound  while (mask&b)>0: we calcul a--> the sum without carry with xor , and b carry with add and shifted to left by one , we return (mask&a) if b is positif else a . 
#o(1) space and time 
        mask= 0xffffffff
        while (mask&b)>0:
            a, b = a ^ b, (a & b) << 1
        return (mask&a) if b>0 else a    

        # return a gives a tle cuz we are not boud with 32 bits in python