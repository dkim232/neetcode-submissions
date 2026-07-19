class Solution:
    def rob(self, nums: List[int]) -> int:
        val1 = nums[0]
        if len(nums) < 2:
            return val1
        val2 = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            cur = max(nums[i] + val1, val2)

            temp = val2
            val2 = cur
            val1 = temp
        
        return val2