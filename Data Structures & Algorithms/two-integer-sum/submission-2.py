class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        
        for i, val in enumerate(nums):
            desiredVal = target - val

            if desiredVal in hashMap:
                return [hashMap[desiredVal], i]
            
            hashMap[val] = i
        
        return 
