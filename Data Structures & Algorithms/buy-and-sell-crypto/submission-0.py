class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        boughtPrice = prices[0]

        for price in prices:
            if price < boughtPrice:
                boughtPrice = price
            else:
                profit = price - boughtPrice
                maxProfit = max(maxProfit, profit)

        return maxProfit