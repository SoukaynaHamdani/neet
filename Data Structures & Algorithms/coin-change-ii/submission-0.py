class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Plan: 1D Space-Optimized Bottom-Up DP
        - Create a 1D array `dp` of size (amount + 1) initialized to 0, where
          dp[i] represents the number of combinations to make up amount `i`.
        - Base case: dp[0] = 1 (there is 1 way to make amount 0: pick no coins).
        - Iterate through each `coin` in the outer loop (ensuring combinations,
          not permutations, are counted):
            * Iterate through each target amount `i` from 1 to `amount`.
            * If `i - coin >= 0`, add the ways to form `i - coin` (taking the
              current coin) to the existing ways in `dp[i]` (not taking it).
        - Return dp[amount] (dp[-1]) as the total number of combinations.

        Time Complexity:  O(n * amount) ->  n = len(coins) 
        Space Complexity: O(amount)  
        """
        # Initialize DP array with 0s
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make 0 with whatever coins: by not choosing any

        for coin in coins:
            for i in range(1, amount + 1):  # i is the current target amount (1 to amount)
                if i - coin >= 0:
                    dp[i] = dp[i] + dp[i - coin]

        return dp[-1]