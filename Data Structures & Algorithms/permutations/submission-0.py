class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, vals):
            #base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            #vals = list of values that we can still choose from
            #del mylist[0]
            for val in vals.copy():
                cur.append(val)
                vals.remove(val)
                backtrack(cur, vals)

                cur.remove(val)#or just remove from end
                vals.append(val)
        backtrack([], nums.copy())
        return res
