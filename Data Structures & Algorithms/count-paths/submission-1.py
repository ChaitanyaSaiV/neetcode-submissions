class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m, n, 0, 0, {})
    def _uniquePaths(self, m: int, n: int, i, j, memo) -> int:
        key = (i, j)
        if key in memo:
            return memo[key]
        
        if i > m - 1 or j > n - 1:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        neighbors = [
            (i + 1, j),
            (i, j + 1)
        ]
        ways = 0
        for neighbor in neighbors:
            ways += self._uniquePaths(m, n, neighbor[0], neighbor[1], memo)
        
        memo[key] = ways
        return memo[key]
