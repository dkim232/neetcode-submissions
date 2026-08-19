class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #val = key, index = value

        for i, val in enumerate(nums):
            #want: difference in map
            if (target - val) in map.keys():
                return [map[target-val], i]
            
            #not in map, insert into map
            map[val] = i
        
        return