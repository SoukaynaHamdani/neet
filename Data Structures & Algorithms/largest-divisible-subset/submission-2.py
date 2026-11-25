class Solution:
        def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
 

            arr.sort()    # backwards  dp memoazation , recuursion 
            cach={}
            
            def dfs(i): 
                if i==len(arr): return []
                if i in cach: return cach[i]

                res=[arr[i]]
                for j in range(i+1,len(arr)):
                    if arr[j]% arr[i]==0: 
                        temp= [arr[i]] + dfs(j)   #o(32)
                     
                        if len(temp)> len(res):
                            res=temp
                cach[i]=res
                return res 
                    
            res=[]     
            for i in range(len(arr)):
                tmp=dfs(i)     
                if len(tmp)> len(res):
                    res=tmp 
            return res     



















"""
#O(N^2) Time and  O(N) Space.  #forward  3 arrays arr --> the value ,dp-->stors the leng of subset  , hash-->stores prev 
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()    #has the values 
        n = len(arr)
        dp = [1] * n  #stores the max subsequence lenght 
        hash_arr = list(range(n))  # Each index initially points to itself [0,1,2,3 ....]

        maxi = 1
        last_index = 0

        for i in range(1, n):
            for j in range(i): #update the len and prev 
                if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    hash_arr[i] = j

            if dp[i] > maxi:  #update max len and last index
                maxi = dp[i]
                last_index = i

        # Reconstruct the subset by walking backward through hash_arr
        res = [arr[last_index]]
        while hash_arr[last_index] != last_index:
            last_index = hash_arr[last_index]
            res.append(arr[last_index])

        return res[::-1]   #we need to reverse it 

 
"""


