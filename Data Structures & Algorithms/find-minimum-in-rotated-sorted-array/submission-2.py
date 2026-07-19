class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')

        left = 0
        right = len(nums) - 1

        if (nums[left] < nums[right]):
            return nums[left]

        while left <= right:
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[right]: #search right
                left = mid + 1
            else: # nums[mid] > nums[left]:
                right = mid - 1
        
        return res
