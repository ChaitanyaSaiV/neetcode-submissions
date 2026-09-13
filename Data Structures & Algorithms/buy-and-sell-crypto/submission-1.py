class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        bought_price = float("inf")

        for price in prices:
            if price < bought_price:
                bought_price = price
            else:
                current_profit = price - bought_price
                profit = max(current_profit, profit)
        
        return profit
