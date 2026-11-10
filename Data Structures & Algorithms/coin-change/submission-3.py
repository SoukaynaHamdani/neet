class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        
        DP Bottom-Up (Tabulation)
        Time: O(len(coins) * amount)
        Space: O(amount)
        
        sort--min is inf for coin diff=amnt-coin minn is the min of minn and 1+f(diff) after the for loop on coins we add to the memo the memo[amnt]=minn
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
            


