class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        
        DP Bottom-Up (Tabulation)
        Time: O(len(coins) * amount)
        Space: O(amount)
        
        sort--  
        for i in range(1,amount+1): min is inf for coin diff=i-coin 
         minn= min(minn,1+ dp[diff])  and dp[i]=minn 
        """


        coins.sort()
        dp=[0]*(amount+1) #0 coins-- min coins is 0 to change it 

         
        
        for i in range(1,amount+1):
            minn=float("inf")
            for coin in coins:
                diff=i-coin
                if diff<0: 
                    break 
                minn= min(minn,1+ dp[diff])   
            dp[i]=minn
        
        result= dp[amount]
        if result<float("inf"):
            return result 
        else: 
            return -1 
            


