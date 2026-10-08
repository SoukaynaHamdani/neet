class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        in : arr heights 
        out:  max of amnt of water  , diff of indecices is the width and the min of hight is and the hight
        2 pointers 
        move the pointer at the min height
        """
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res