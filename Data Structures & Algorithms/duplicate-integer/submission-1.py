class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        indepSet = set(nums)
        if len(indepSet) != len(nums):
            return True
        return False
            
            