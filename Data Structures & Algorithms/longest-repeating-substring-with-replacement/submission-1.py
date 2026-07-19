class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqDict = defaultdict(int)
        maxFreq = 0
        res = 0

        for right in range(len(s)):
            freqDict[s[right]] += 1
            maxFreq = max(maxFreq, freqDict[s[right]])

            while (right - left + 1) - maxFreq > k:
                freqDict[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res