class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if (prices[right] > prices[left]):
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else: #right <= left
                left = right
            right += 1
        
        return maxProfit