class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen= set()
        for num in nums:
            if num in seen:
                return True
            else:
             seen.add(num)
        return False 
# Create the object
sol = Solution()

# Call the method from the object
print(sol.hasDuplicate([1, 2, 3, 3]))