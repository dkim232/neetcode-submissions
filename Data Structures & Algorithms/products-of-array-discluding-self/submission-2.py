class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefProd = [1] * length
        suffProd = [1] * length

        prefix = 1
        for i in range(1, length):
            prefix *= nums[i-1]
            prefProd[i] = prefix
        
        suffix = 1
        for i in range(length-2, -1, -1):
            suffix *= nums[i+1]
            suffProd[i] = suffix
            
        res = []
        for i in range(length):
            res.append(prefProd[i] * suffProd[i])
        
        return res