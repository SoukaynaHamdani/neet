class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        """bottom up dp -tabulation 
        KEEP  trck of i,  
        for each i start from the end of the string, we have (nmbr of wors in dict) desicions. for each word if (i+len(word))<=len(s) in bound  and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)] we see if the rest of the string is true 
        return dp[0] 
        
        Time: O(n * m * k) | n = len(s), m = len(wordDict), k = avg word length
        Space o(n) memory of dp list """
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True #base case: empty string after the last character is valid

        for i in range(len(s)-1,-1,-1): #start from the last char len(s)-1
            for word in wordDict: 
                if (i+len(word))<=len(s) and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)]
                if dp[i]: #if first word gave us true no need to check the second 
                    break
        return dp[0]