class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target: #overshot; shrink to first half
                right = middle - 1
            else: #middle < target; undershot
                left = middle + 1
        return -1       