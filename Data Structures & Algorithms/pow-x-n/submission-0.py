class Solution:
    def myPow(self, x: float, n: int) -> float:
        cur = x

        isNegative = False
        if n < 0:
            isNegative = True
            n = -1 * n
        if n == 0:
            return float(1)

        for i in range(n-1):
            cur = cur * x
        
        if isNegative:
            cur = 1 / cur
        
        return cur