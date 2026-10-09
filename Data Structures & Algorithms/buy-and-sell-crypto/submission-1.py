class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        arr 
        out : max profit 
        edge case not tran
        """
        l=0
        r=0
        maxp=0
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                pass
            elif prices[l]>prices[r]:
                l+=1
            maxp=max(maxp,prices[r]-prices[l])
        return maxp