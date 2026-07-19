class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)

        left = 0
        right = windowSize - 1
        freqDict1 = Counter(s1)
        freqDict2 = defaultdict(int)

        for i in range(windowSize-1):
            freqDict2[s2[i]] += 1
        

        while right < len(s2):#until right reaches the end
            freqDict2[s2[right]] += 1

            if freqDict1 == freqDict2:#freq dicts different
                return True
    
            freqDict2[s2[left]] -= 1
            if freqDict2[s2[left]] == 0:
                freqDict2.pop(s2[left])
            left += 1
            right += 1
        
        return False