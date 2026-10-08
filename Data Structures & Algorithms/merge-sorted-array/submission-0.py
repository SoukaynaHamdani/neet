class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)): 
            m=len(nums1)
            n=len(nums2)
            p1=m-n-1
            p2=n-1
            e=m-1
            if nums2[p2]>nums1[p1]:
                nums1[e]=nums2[p2]
            else:
                nums1[e]=nums1[p1]
            p1-=1
            p1-=1
