class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0 #answer index
        for i in range(len(nums)):
            if nums[i] != val: #pass
                nums[j] = nums[i]
                j += 1
            else: #fail; nums[i] == val:
                continue

        return j