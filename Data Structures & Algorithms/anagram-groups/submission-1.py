class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            freqArr = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                freqArr[index] += 1
            tup = tuple(freqArr)
            ans[tup].append(word)
        return list(ans.values())