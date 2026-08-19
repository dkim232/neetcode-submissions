class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = Counter(list(s))
        freqMapT = Counter(list(t))

        return freqMapS == freqMapT