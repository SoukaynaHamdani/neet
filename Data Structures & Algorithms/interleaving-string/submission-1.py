class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """plan: bottom up dp  we start a 2 d grid filled with false 
        - Edge case: if len(s1) + len(s2) != len(s3), return False.
        - Create an (n + 1) x (m + 1) grid filled with False

        base case dp[len(s1)][len(s2)]= True  both i1 and i2 outofbond meaning we reached the end of s3 (i3= i1+i2)
        - Fill bottom-right to top-left:
        if i in bound and character at i in s1 is equal to char at i+j in s3 and the position below me (next row) is true (if we choose i we can make the rest of s3 using the remaining characters of s1 and s2 
        if i<len(s1)  and s1[i]==s3[i +j] and  dp[i+1][j]:
                    dp[i][j]=True 
        same for j but we go right(next column) ) 
        return dp[0][0]
        Time Complexity:  O(n * m) -> fills an (n + 1) x (m + 1) grid 
        Space Complexity: O(n * m)  
        """

        n=len(s1)
        m=len(s2)
        if n+m!=len(s3):
            return False 

        dp=[[False]* (m+1) for i in range(n+1)]
        dp[len(s1)][len(s2)]= True 
        for i in range(n,-1,-1):
            for j in range (m , -1 , -1 ):

                if i<len(s1)  and s1[i]==s3[i +j] and  dp[i+1][j]:
                    dp[i][j]=True 
                if j<len(s2)  and s2[j]==s3[i +j] and  dp[i][j+1]:
                    dp[i][j]=True 
        return dp[0][0]



"""
# memo aproach same compl but use recursiom 
if len( s1) + len(s2) != len(s3):
            return False
memo={}
def dfs(i,j):
    if fi==len(s1) and j ==len(s2):
        return True 
    if (i,j) in memo: 
        return memo[(i,j)] 

    if i<len(s1)  and s1[i]==s3[i +j] and  dfs(i+1,j):
                    return True 
    if j<len(s2)  and s2[j]==s3[i +j] and  dfs(i,j+1):
        return True
    memo[(i,j)]=False
    return false
return dfs(0,0) 
""" 