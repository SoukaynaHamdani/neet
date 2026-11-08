class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1,rob2=0,0   
        for n in nums:
            rob1,rob2=rob2 , max(n+rob1,rob2)    
        return rob2   

"""time:o(n) space: o(1)  Pattern: DP (Include / Exclude)-bottom up constant space
        
    State Tracking:
    rob1: Max mony collected up to house (i - 2).
    rob2: Max  up to house (i - 1).
    
    At Current House n :Two Choices:
    1-Rob house  n: + best loot from (i - 2) (n + rob1), skipping the adjacent house rob2.
    
    2-Skip house n: Keep the best profit achieved at the adjacent house (rob2).
    
    Optimal Choice:new_rob = max(n + rob1, rob2)
            
            # Shift variables forward
            rob1 = rob2
            rob2 = new_rob
     Once the loop finishes, rob2 holds the global maximum profit.
        """
            
         

                


