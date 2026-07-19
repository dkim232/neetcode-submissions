class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        freqt = Counter(t)
        res = ""
        windowFreq = Counter()

        while right < len(s):
            windowFreq[s[right]] += 1
            #window valid?
            while freqt <= windowFreq: #while window is valid, move left
                curString = s[left:right+1]
                if res == "" or len(curString) < len(res):
                    res = curString
                windowFreq[s[left]] -= 1
                left += 1
            right += 1
        return res