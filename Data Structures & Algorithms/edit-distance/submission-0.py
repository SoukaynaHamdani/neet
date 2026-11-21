class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1] * m for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            # Base cases: one string is exhausted, insert/delete remaining chars of the other
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] != word2[j]:
                dp[i][j] = 1 + min(
                    dfs(i, j - 1),      # Insert
                    dfs(i - 1, j),      # Delete
                    dfs(i - 1, j - 1)   # Replace
                )
            else:
                dp[i][j] = dfs(i - 1, j - 1)

            return dp[i][j]

        return dfs(n - 1, m - 1)