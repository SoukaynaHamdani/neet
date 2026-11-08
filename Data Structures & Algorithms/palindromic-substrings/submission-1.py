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

                    