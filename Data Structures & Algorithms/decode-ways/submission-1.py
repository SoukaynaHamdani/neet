class Solution:
    def numDecodings(self, s: str) -> int:
        """
        DP Bottom-Up with Rolling Variables
        Time: O(n)
        Space: O(1)
        """
        if not s or s[0] == "0":
            return 0

        # prev2 represent dp[0] (empty prefix)
        # prev1 represent dp[1] (first character)
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            current = 0

            #onedegit
            if s[i] != "0":
                current += prev1

            #twodigits
            two_digits = int(s[i - 1 : i + 1])
            if 10 <= two_digits <= 26:
                current += prev2

            
            prev2 = prev1
            prev1 = current

        return prev1





"""class Solution:
    def numDecodings(self, s: str) -> int:
         
        DP Bottom-Up (Tabulation)
        Time: O(n)
        Space: O(n)
        

        if not s or s[0]=="0":
            return 0 
        n=len(s)
        
        dp=[0]*(n+1)         #n+1 cuz the 0 th index of my string will be at position 1 in dp cuz its length is 1 , for the 0 th index in dp is for nbr ways to decoding an empty string. 
        #dp[i] represents: "How many valid ways to decode the prefix string  of length  i ."

        dp[0]= 1 #valid decodings for a prefix of length0 (empty string "").
        dp[1]=1  #valid decodings for a prefix of length 1 (just s[0]).
        # dp[2] = valid decodings for a prefix of length  2 (s[0:2], which includes s[1]).  The character at index 1 (s[1]) is never evaluated at dp[1]; it is evaluated when calculating dp[2].

        
        for i in range(2,n+1):
            onedigit=int(s[i-1]) #the current number in the string but i is indexes of dp so we de -1 
            twodigits=int(s[i-2:i])      

            if 1 <= onedigit <= 9:
                dp[i] += dp[i - 1]
            
            if 10 <= twodigits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

"""