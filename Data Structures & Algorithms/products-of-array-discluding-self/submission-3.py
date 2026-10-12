class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        pref = 1

        for i in range(1, len(nums)):
            pref *= nums[i-1]
            res.append(pref)
        
        suff = 1
        for i in range(len(nums)-2, -1, -1):
            suff *= nums[i+1]
            res[i] *= suff
        
        return res