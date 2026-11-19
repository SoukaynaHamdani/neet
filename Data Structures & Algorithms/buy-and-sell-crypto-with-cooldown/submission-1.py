class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """ 
          
 Plan: 2D DP with memoization (decision tree)
        - dp = {}  # key = (i, buying), val = max profit
          Maps the day index and state to the maximum profit:
            * buying == True:  choice to buy or cooldown
            * buying == False: choice to sell or cooldown
        - Base case: if i is out of bounds  return 0
        - Memoization: if (i, buying) is in dp, return its cached value
        - Transitions:
            * cooldown = recursion(i + 1, buying)
            * if buying is True:
                buy = recursion(i + 1, not buying) - prices[i]  # transitions to False
                if buying is true : dp[(i,buying)] max btween buy and coldown 
        
                
            * else (buying is False):
                sell = recursion(i + 2, not buying) + prices[i] 
                 # transitions to True (i + 2 due to mandatory cooldown)
                dp[(i, buying)] = max(sell, cooldown)
    time and space o(n)
            
             
 """
        

        dp = {}  # key = (i, buying), val = max profit

        def recursion(i, buying):  # buying == True means we have the choice to buy or cooldown
            # Base case
            if i >= len(prices):
                return 0

            # Memoization
            if (i, buying) in dp:
                return dp[(i, buying)]
 
            cooldown = recursion(i + 1, buying)
            if buying:
                buy = recursion(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)

            else:  # not buying (buying == False): we hold a stock, so we can't buy
                sell = recursion(i + 2, not buying) + prices[i] 
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return recursion(0, True)