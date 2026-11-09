class Solution:
    def numDecodings(self, s: str) -> int:
        """
        DP Bottom-Up (Tabulation)
        Time: O(n)
        Space: O(n)
        """

        if not s or s[0]=="0":
            return 0 
        n=len(s)
        
        dp=[0]*(n+1)
        #dp[i] represents: "How many valid ways to decode the prefix of length $i$."

        dp[0]= 1 #valid decodings for a prefix of length0 (empty string "").
        dp[1]=1  #valid decodings for a prefix of length 1 (just s[0]).
        # dp[2] = valid decodings for a prefix of length $2$ (s[0:2], which includes s[1]).  The character at index 1 (s[1]) is never evaluated at dp[1]; it is evaluated when calculating dp[2].

        # dp[i] i is the lenght of the string
        for i in range(2,n+1):
            onedigit=int(s[i-1])
            twodigits=int(s[i-2:i])

            dp[i]+=dp[i-1] if 0<onedigit<10  else 0
            
            dp[i]+=dp[i-2] if 10<=twodigits<=26  else 0

        return dp[n]

