class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #2 arrays: prefix prod, suffix prod 
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length

        prefixProd = 1
        for i in range(1, length):
            prefixProd *= nums[i-1]
            prefix[i] = prefixProd

        suffixProd = 1
        for i in range(length-2, -1, -1):
            suffixProd *= nums[i+1]
            suffix[i] = suffixProd
        
        res = []
        for i in range(length):
            res.append(prefix[i] * suffix[i])
        
        return res

            
