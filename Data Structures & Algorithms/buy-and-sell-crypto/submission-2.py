class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        boughtPrice = float("inf")
        profit = 0

        for price in prices:
            if boughtPrice > price:
                boughtPrice = price
                continue
            else:
                currentProfit = price - boughtPrice
                profit = max(profit, currentProfit)
            
        return profit