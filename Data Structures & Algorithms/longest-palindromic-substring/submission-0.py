class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while (left >= 0) and (right < len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]#since we are on failed condition
        
        res = s[0]
        for i in range(len(s)):
            evenString = expand(i, i+1)
            oddString = expand(i, i)

            if len(evenString) > len(res):
                res = evenString
            if len(oddString) > len(res):
                res = oddString
            
        return res