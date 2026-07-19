class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        left = 0
        right = windowSize-1
        s1freq = Counter(s1)
        s2freq = defaultdict(int)

        for i in range(windowSize-1):
            s2freq[s2[i]] += 1

        while right < len(s2):
            s2freq[s2[right]] += 1

            if s1freq == s2freq:
                return True
            
            s2freq[s2[left]] -= 1
            if s2freq[s2[left]] == 0:
                s2freq.pop(s2[left])
            left += 1
            right += 1
        
        return False