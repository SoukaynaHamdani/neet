class Solution:
    def climbStairs(self, n: int) -> int:
        """Bottom up -constant space
        Time Complexity: O(n)
        Space Complexity: O(1)"""
        two =1     
        one=1     
        
        for i in range(n-1): #n-1 exclusive 
            two, one = one , two+one 
        return one 
