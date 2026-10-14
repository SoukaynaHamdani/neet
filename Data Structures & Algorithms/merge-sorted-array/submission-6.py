class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1  #last valid elem in nums1
        p2=n-1  #last elem in nums 2 
        e=m+n-1 #last elem in nums1
        while p2>=0:   
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[e]= nums1[p1]
                p1-=1
            else:    # p1<0 / p1>0 and  nums2[p2]>nums1[p1]
                nums1[e]= nums2[p2]
                p2-=1
            e-=1
        
