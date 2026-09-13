class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self._longestCommonSubsequence(text1, text2, 0, 0, {})
    def _longestCommonSubsequence(self, text1: str, text2: str, i, j, memo) -> int:
        key = (i, j)
        if key in memo:
            return memo[key]
        
        if i == len(text1) or j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            memo[key] = 1 + self._longestCommonSubsequence(text1, text2, i + 1, j + 1, memo)
        else:
            memo[key] = max((self._longestCommonSubsequence(text1, text2, i + 1, j, memo)), (self._longestCommonSubsequence(text1, text2, i, j + 1, memo)))

        return memo[key]
        