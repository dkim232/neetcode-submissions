class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted = strs.sort()
        res = ""

        #shortest is index 0
        first = strs[0]

        for i, char in enumerate(first):
            matching = True
            for string in strs[1:]:
                if string[i] != char:
                    matching = False
                    break
                #else, string is ok. continue to next string in the list
            #after iterating through all the other strings, they all ahve the same?
            if matching == True:
                res += char
                continue
            else:
                break
        return res