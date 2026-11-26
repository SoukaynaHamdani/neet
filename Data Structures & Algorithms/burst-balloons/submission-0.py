class Solution:
    #top down 
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