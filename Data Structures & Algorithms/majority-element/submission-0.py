class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                cand = num
                count += 1
            elif num == cand: #reinforce
                count += 1
            else: #decrement
                count -= 1
        return cand