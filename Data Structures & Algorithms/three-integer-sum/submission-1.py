class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numvals = len(nums)
        nums.sort()
        target = 0
        res = []
        for i in range(numvals-2):
            if (i >= 1) and (nums[i-1] == nums[i]):
                continue
            val1 = nums[i]
            left, right = i+1, numvals-1

            while (left < right):
                sumval = val1 + nums[left] + nums[right]

                if sumval < target:
                    left += 1
                    continue
                
                elif sumval > target:
                    right -= 1
                    continue
                               
                tup = [val1, nums[left], nums[right]]
                res.append(tup)
                left += 1
                right -= 1
                while (left < right) and (left > i+1) and (nums[left] == nums[left-1]):
                    left += 1
                while (left < right) and (right < numvals-1) and (nums[right] == nums[right+1]):
                    right -= 1
        
        return res

