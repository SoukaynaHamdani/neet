class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """  we start from bottom right corner and we go left . if They mtch --> +1 + diagnal dp[i][j]+= 1+dp[i+1][j+1]

         if they dont match we take the max of right and down    we only need 2 rows 
return the value at top left dp[0][0]
space and time o (n*m)""" 
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]  # we add the diagonal 
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[0][0]