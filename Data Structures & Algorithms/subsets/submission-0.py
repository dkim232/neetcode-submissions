class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        
        def backtrack(start, cur):
            if start >= len(nums):
                res.append(cur.copy())
                return
            
            ## add/don't add to cur (subset)
            # add:
            cur.append(nums[start])
            backtrack(start+1, cur) #add

            cur.pop()
            backtrack(start+1, cur) #don't add start index to cur

        
        backtrack(0, [])

        return res