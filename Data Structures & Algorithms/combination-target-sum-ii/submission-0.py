class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, curSet):
            print(index, curSet)
            #base case
            if sum(curSet) == target:
                res.append(curSet.copy())
                return
            if index >= len(candidates):
                return            
            elif sum(curSet) > target:
                return
            else:
                curSet.append(candidates[index])
                backtrack(index+1, curSet)
                curSet.pop()
                while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
                    index += 1
                backtrack(index+1, curSet)
        
        backtrack(0, [])
        return res
            