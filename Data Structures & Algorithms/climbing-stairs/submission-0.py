class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n, 0, {})
    def _climbStairs(self, n, index, memo) -> int:
        if index in memo:
            return memo[index]
        if index == n:
            return 1

        if index > n:
            return 0
        
        including_first = self._climbStairs(n, index + 1, memo)
        excluding_first = self._climbStairs(n, index + 2, memo)

        memo[index] = including_first + excluding_first

        return  memo[index]