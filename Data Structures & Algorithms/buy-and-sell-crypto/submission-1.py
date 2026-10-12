class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = 1

        while r < len(prices):
            diff = prices[r] - prices[l]
            if (diff > 0):
                res = max(res, diff)
            else: #buy > sell
                l = r
            r += 1
        
        return res