class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqList1 = defaultdict(int)
        freqList2 = defaultdict(int)
        
        for char in s:
            freqList1[char] += 1
        
        for char in t:
            freqList2[char] += 1
              

        if freqList1 == freqList2:
            return True
        return False