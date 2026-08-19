class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * 2 * l

        for i, val in enumerate(nums):
            res[i], res[i+l] = val, val
        
        return res
