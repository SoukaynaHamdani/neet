class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """XOR numbers in nums with indecies , same numbers cancel , we left with the missing 

        start res to last elemnt (len(nums)) then add (i-nums[i])  for i in len(nums) 
        o(n)time , o(1) space """
        res=len(nums)
        for i in range(len(nums)):
             res+=(i-nums[i])   #or  res ^= i ^ nums[i]
        return res 

    
    """
    class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)
    """