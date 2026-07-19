class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                count[index] += 1
            resIndex = tuple(count)
            res[resIndex].append(string)
        
        return list(res.values())

