class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        lastSeen = {}

        for right in range(len(s)):
            while s[right] in s[left:right]:
                location = lastSeen[s[right]]
                left = location + 1
            lastSeen[s[right]] = right
            maxLen = max(maxLen, right-left+1)
        
        return maxLen