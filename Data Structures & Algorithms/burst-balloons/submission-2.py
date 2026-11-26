class Solution:

     def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        a= [1]+nums+[1]
        dp=[[0]*(n+ 2) for _ in range(n+2)]

        for i in range(n,0,-1): 
            for j in range(1,n+1):
            #no subproblams 
                if (i>j):
                    continue 
        
                maxi = float('-inf')
                for indx in range(i,j+1):

                    cost= (a[i-1] * a[indx]* a[j+1]
                    +dp[i][indx-1]
                    +dp[indx+1] [j])

                    maxi=max(maxi,cost)
                    
                dp[i][j]=maxi 
        return dp[1][n]


"""
    #top down-  using memo with 2d dp[i][j]  doesnt give tle while a dict  does  
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        a= [1]+nums+[1]
        dp=[[-1]*(n+ 1) for _ in range(n+1)]
        def f(i,j):
            #no subproblams 
            if (i>j):
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            maxi = float('-inf')
            for indx in range(i,j+1):

                cost= (a[i-1] * a[indx]* a[j+1]
                +f(i,indx-1)
                +f(indx+1, j))

                maxi=max(maxi,cost)
                
            dp[i][j]=maxi
            return dp[i][j] 
        return f(1,n)

"""




"""
    #top down gives tle 
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        a= [1]+nums+[1]
        memo={}
        def f(i,j):
            if (i,j) in memo: 
                return memo[(i,j)]
            #no subproblams 
            if (i>j):
                return 0

            maxi = float('-inf')
            for indx in range(i,j+1):

                cost= (a[i-1] * a[indx]* a[j+1]
                +f(i,indx-1)
                +f(indx+1, j))

                maxi=max(maxi,cost)
                
            memo[(i,j)]=maxi
            return memo[(i,j)] 
        return f(1,n)

"""