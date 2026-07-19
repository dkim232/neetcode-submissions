class Solution:
    def climbStairs(self, n: int) -> int:
        cur1 = 1
        cur2 = 2
        if n == 1:
            return cur1
        if n == 2:
            return cur2

        for i in range(3,n+1):
            cur3 = cur1 + cur2
            
            temp = cur2
            cur2 = cur3
            cur1 = temp
        
        return cur3