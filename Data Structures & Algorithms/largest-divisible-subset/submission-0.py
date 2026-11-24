class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()    #has the values 
        n = len(arr)
        dp = [1] * n  #stores the max subsequence lenght 
        hash_arr = list(range(n))  # Each index initially points to itself [0,1,2,3 ....]

        maxi = 1
        last_index = 0

        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    hash_arr[i] = j

            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i

        # Reconstruct the subset by walking backward through hash_arr
        res = [arr[last_index]]
        while hash_arr[last_index] != last_index:
            last_index = hash_arr[last_index]
            res.append(arr[last_index])

        return res[::-1]   #we need to reverse it 