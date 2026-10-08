class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        dev=1
        if x>dev*10:
            dev*=10
        left=x//dev
        right=x %10
        if left !=right:
            return False
        x= (x%dev)//10
        dev = dev /100
        return True
