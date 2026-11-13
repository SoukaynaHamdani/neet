class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        """bottom up dp -tabulation 
        KEEP  trck of i,  
        for each i start from the end of the string, we have (nmbr of wors in dict) desicions. for each word if (i+len(word))<=len(s) in bound  and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)] we see if the rest of the string is true 
        return dp[0] 
        
        Time : o(n * m  * k) n=len of string , m is nmbr of words in wordDict , k is average len of words in wordDict 
        Space o(n) memory of dp list """
        
        dp=[False]*(len(s)+1)
        dp[len(s)+1]=True #base case "" after our last char in s

        for i in range(len(s)-1,-1,-1): #start from the last char len(s)-1
            for word in wordDict: 
                if (i+len(word))<=len(s) and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)]
                if dp[i]: #if first word gave us true no need to check the second 
                    break
        return dp[0]