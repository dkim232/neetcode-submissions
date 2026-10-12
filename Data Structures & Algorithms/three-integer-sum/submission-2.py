class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        target = 0
        res = []

        for i in range(length-2):
            if (i >= 1) and (nums[i] == nums[i-1]): #if repeat first num,
                continue
            
            #not a repeat: begin checking
            l,r = i+1, length-1
            
            while (l < r):
                total = nums[i] + nums[l] + nums[r]

                if (total < 0):
                    l += 1
                    continue

                if (total > 0):
                    r -= 1
                    continue
                
                #here, l<r AND total == 0
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while (l < r) and (nums[l] == nums[l-1]):
                    l += 1
                while (l < r) and (nums[r] == nums[r+1]):
                    r -= 1
        return res
            