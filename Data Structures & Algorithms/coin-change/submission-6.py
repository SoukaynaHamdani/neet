class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        
        DP Bottom-Up (Tabulation)
        Time: O(len(coins) * amount)   #len(dp) * nmbr of coins 
        Space: O(amount)
        
        sort--  
        for i in range(1,amount+1): min is inf for coin diff=i-coin 
         minn= min(minn,1+ dp[diff])  and dp[i]=minn if we can t make an amount with coin dp[i]=minn  gets the float("inf")
        """
 
        coins.sort()  # O(k log k)  k nmbr of coins 
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break  
                dp[i] = min(dp[i], 1 + dp[diff])
                
        return dp[amount] if dp[amount] < float("inf") else -1



"""
        coins.sort()
        dp=[0]*(amount+1) #0 coins-- min coins is 0 to change 0
        
        for i in range(1,amount+1):
            minn=float("inf")
            for coin in coins:
                diff=i-coin
                if diff<0: 
                    break 
                minn= min(minn,1+ dp[diff])   
            dp[i]=minn
        
         
        if dp[amount]<float("inf"):
            return dp[amount] 
        else: 
            return -1 
            


"""