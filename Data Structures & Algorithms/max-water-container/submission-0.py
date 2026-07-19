class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        res = (right - left) * min(heights[left], heights[right])

        while left < right:
            curval = (right - left) * min(heights[left], heights[right])
            res = max(res, curval)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res