class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("∞")
            res.append(s)
        return "".join(res)  #make the list 1 joined string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #index pointer

        while i < len(s):
            j = i
            while s[j] != "∞": #keep going until end of length
                j += 1
            length = int(s[i:j]) #length as may be more than 1 character
            i = j + 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j
        return res