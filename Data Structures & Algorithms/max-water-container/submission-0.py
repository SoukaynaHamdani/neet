class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        in : arr heights 
        out:  max of amnt of water  , diff of indecices is the width and the min of hight is and the 
        2 pointer 
        move the pointer at the min height
        """
        l=0
        r=len(heights)-1
        max_water=0
        while l<r :
            curr_water=(min(heights[l],heights[r]))*(r-l)
            if min(heights[l],heights[r])==heights[l]:
                l+=1
            elif  min(heights[l],heights[r])==heights[r]:
                r-=1
            max_water=max(max_water,curr_water)
        return max_water      