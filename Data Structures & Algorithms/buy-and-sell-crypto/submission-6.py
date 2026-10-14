class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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