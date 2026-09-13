class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        i = 1
        while i < len(prices):
            current_profit = prices[i] - buy_price
            max_profit = max(current_profit, max_profit)
            buy_price = min(buy_price, prices[i])
            i += 1
        return max_profit