class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #1 string delimited by spaces
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 #slide right window until we reach delimiter
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res


            
