class Solution:
    def countSubstrings(self, s: str) -> int:
        """ Time Complexity: O(n^2)  Space Complexity: O(1)"""
        
        l=0
        r=0
        nbr=0

        for i in range(len(s)):
            l,r=i,i
             
            while l>=0 and r<len(s) and s[l]==s[r]:
                    l-=1
                    r+=1
                    nbr+=1
            
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                    l-=1
                    r+=1
                    nbr+=1
        return nbr


"""  class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        nbr = 0

        def count_palindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(n):
            nbr += count_palindromes(i, i)      # Odd length
            nbr += count_palindromes(i, i + 1)  # Even length

        return nbr  """


""" 
DP bottom up - tabulation , Time complexity: O(n ^2) space and time 
class Solution:
    def countSubstrings(self, s):
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):      
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res"""

                    