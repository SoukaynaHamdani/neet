class Solution:

    """ DP at each position i consider selling, i keep track of the minBuy  in the left of me and it is going to be the max profit if i am selling at that day  """
    def maxProfit(self, prices: List[int]) -> int: 
        maxP = 0
        minBuy = prices[0]

        for i  in range(len(prices)):       #prices[i] or sell 
            maxP = max(maxP, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return maxP

"""
 sliding window 


        find position where to buy low first and 
        from there calc the max profit use l ,r pointers 
        l=0
        r=1
         maxPr=0
         while r<len(prices):
            if prices[r]<=prices[l]: #buy low
                l=r
            else:
                maxPr=max(maxPr,prices[r]-prices[l])
            r+=1
         return  maxPr

"""