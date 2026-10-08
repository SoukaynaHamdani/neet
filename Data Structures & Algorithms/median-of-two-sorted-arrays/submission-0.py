class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A=nums1
        B=nums2
        if len(B)>len(A):
            A, B = B,A 
        l=0
        r=len(A)-1
        total = len(nums1)+len(nums2)
        half = total //2     # half LEFT = left partition + left partition of B 
        while True:
            i=(l+r)//2#the position of the last element in the left partition of A
            j=half-i-2 #the position of last element in the left partition of B
            
            Aleft=A[i] if i>=0 else float("-infinitiy")
            Aright=A[i+1] if (i+1)<len(A) else float("+infinitiy")
            Bleft=B[i] if i>=0 else float("-infinitiy")
            Bright=B[i+1] if (i+1)<len(B) else float("+infinitiy")
            
            if Aleft <= Bright and Bleft<= Aright:
                #odd 
                if total %2:
                    return min(Aright , Bright)   #min of the rights 
                else:
                    return max(Aleft,Bleft)+min(Aright,Bright) //2 