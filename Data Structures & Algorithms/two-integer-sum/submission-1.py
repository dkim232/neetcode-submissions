class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, val in enumerate(nums):
            want = target - val
            if want in seen:
                return [seen[want], index]
            
            seen[val] = index
        
        return