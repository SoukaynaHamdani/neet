class Solution:
    def numDistinct(self, s: str, t: str) -> int:



 
        #dp space optimazation O(m)space o(n*m) time
        n=len(s)
        m=len(t)

        # `dp` represents row (i + 1) outside the first loop  
        dp = [0] * (m + 1)
        dp[m] = 1  # Base case: empty suffix of t has 1 match


        for i in range(n-1,-1,-1):
            #outside the second loop 
            nextdp=[0]*(m+1)
            nextdp[m]=1
            for j in range(m-1,-1,-1):
                if s[i]==t[j]:
                    nextdp[j]=dp[j+1]+dp[j]
                else: 
                    nextdp[j]= dp[j]
            dp=nextdp
        return dp[0]

"""
        #2D String Subsequence DP --> 1D In-Place Space Optimization.  O(m)space o(n*m) time
        n=len(s)
        m=len(t)

        dp = [0] * (m + 1)
        dp[m] = 1 

        for i in range(n-1,-1,-1):
            for j in range(m):  # Iterate j FORWARD (0 -> m - 1) so dp[j + 1] still holds row (i + 1)
                if s[i]==t[j]:
                    dp[j]+=dp[j+1] 
        
        return dp[0]

"""



"""
        #dp bottom up o(n*m ) space and time 
        n=len(s)
        m=len(t)

        #(n + 1) x (m + 1) table initialized to 0
        dp=[[0]*(m+1) for _ in range(n+1)]

        # Base case: if j == len(t) (last column), t is completely matched -> 1 way 
        for i in range(n+1): 
            dp[i][m]=1 #last col 
        
        #Fill bottom-right to top-left (reverse of dfs(0, 0) moving to (n, m))
        for i in range(n-1,-1,-1)   :
            for j in range(m-1,-1,-1):

                if s[i]==t[j]:
                    dp[i][j]=dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j]= dp[i+1][j]
        return dp[0][0]


"""




"""
        # DP top down memozation space o(n*m)+O(n+m)   time o(n*m)

        cach={} #indecies (i,j)--> longest way starting at these indecies 
         
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0 
            if (i,j) in cach: 
                return cach[(i,j)]
         
            if s[i]== t[j]:
                cach[(i,j)]=dfs(i+1,j+1)+ dfs(i+1,j)

            else:
                cach[(i,j)]= dfs(i+1,j)
            return cach[(i,j)]
        return dfs(0,0)

"""