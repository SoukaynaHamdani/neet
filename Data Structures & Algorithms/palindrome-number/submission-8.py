class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        dev=1
        if x>dev*10:
            dev*=10
        while x:      ###!!
            left=x//dev
            right=x %10
            if left !=right:
                return False
            x= (x%dev)//10
            dev = dev /100
        return True
