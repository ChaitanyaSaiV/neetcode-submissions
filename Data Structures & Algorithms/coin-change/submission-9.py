class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = self._coinChange(coins, amount, {})
        if min_coins == float("inf"):
            return -1
        else:
            return min_coins
    def _coinChange(self, coins, amount, memo) -> int:
        if amount in memo:
            return memo[amount]
        
        if amount == 0:
            return 0

        if amount < 0:
            return float("inf")
        
        count = float("inf")

        for coin in coins:
            current_count = 1 + self._coinChange(coins, amount - coin, memo)
            count = min(current_count, count)

        memo[amount] = count
        return memo[amount]    