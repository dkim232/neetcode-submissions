class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numWords = len(strs)
        arr = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for char in s:
                curChar = ord(char) - ord("a")
                temp[curChar] += 1
            arr[tuple(temp)].append(s)        
        res = []
        for keyList in arr.values():
            res.append(keyList)
        return res