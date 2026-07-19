class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(index, cur):
            if index >= len(nums):
                return
            if sum(cur) == target:
                res.append(cur.copy())
                return

            elif sum(cur) > target:
                return


            else:
                cur.append(nums[index])
                backtrack(index, cur)
                cur.pop()
                backtrack(index+1, cur)
        
        backtrack(0, [])

        return res
        

                