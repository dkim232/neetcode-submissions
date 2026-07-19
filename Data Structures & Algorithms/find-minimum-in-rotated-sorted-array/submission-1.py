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
            if nums[mid] > nums[left]: #need to go right
                res = min(res, nums[left])
                left = mid + 1
            else: #if nums[mid] <= nums[left]
                res = min(res, nums[right])
                right = mid - 1
        
        return res
