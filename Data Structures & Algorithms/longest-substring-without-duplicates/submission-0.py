class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in s[left:right]:
                left += 1
            maxLen = max(maxLen, len(s[left:right])+1)
        
        return maxLen