class Solution:
    def rob(self, nums: List[int]) -> int:
        val1 = nums[0]
        if len(nums) < 2:
            return val1
        
        val2 = max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            cur = max(nums[i] + val1, val2)
            print(cur)

            temp = val2
            val2 = cur
            val1 = temp

        val3 = nums[1]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        
        val4 = max(nums[2], nums[1])
        for i in range(3, len(nums)):
            cur = max(nums[i] + val3, val4)
            print(cur)

            temp = val4
            val4 = cur
            val3 = temp
        
        return max(val2, val4)
