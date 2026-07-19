class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqDict = defaultdict(int)
        maxLen = 0

        for right in range(len(s)):
            #should fail if:
            freqDict[s[right]] += 1
            while ((right - left + 1) - max(freqDict.values())) > k:#size of window - most frequent
                freqDict[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen