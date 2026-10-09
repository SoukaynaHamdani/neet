class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        arr 
        out : max profit 
        edge case not tran
        """
        l=0
        r=0
        for r in rang(len(prices)):
            if nums [l]<num[r]:
                r+=1
            else:
                l+=1
            

