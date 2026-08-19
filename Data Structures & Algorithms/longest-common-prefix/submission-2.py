class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]

        strs = sorted(strs)
        res = ""
        #shortest is index 0
        first = strs[0]
        last = strs[-1]

        for i, char in enumerate(first):
            if last[i] != char:
                break
            res += char
        
        return res