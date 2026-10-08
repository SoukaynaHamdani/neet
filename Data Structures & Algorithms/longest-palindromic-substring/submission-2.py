class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        max_len = 0
        
        for i in range(len(s)):
            # 1. Odd length (مركز فردي)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res_l, res_r = l, r
                l -= 1
                r += 1
                
            # 2. Even length (مركز زوجي)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res_l, res_r = l, r
                l -= 1
                r += 1
                
        return s[res_l:res_r + 1]