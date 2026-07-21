class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        for i in range(len(strs[0])):
            curChar = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != curChar:
                    return s[:i]
        return strs[0]
