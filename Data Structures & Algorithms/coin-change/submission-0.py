class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo={0:0}  #0 coins-- min 0 to change

         
        def min_coin(amnt): 
            if amnt in memo:
                return memo[amnt]

            minn=float("inf")
            for coin in coins:
                diff=amnt-coin
                if diff<0: 
                    break 
                minn= min(minn,1+ min_coin(diff))   # +1 cuz we used the coin 
            memo[amnt]=minn
            return minn
            
        result= min_coin(amount)
        if result<float("inf"):
            return result 
        else: 
            return -1 
            


