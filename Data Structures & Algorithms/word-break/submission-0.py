class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._wordBreak(s, wordDict, 0, {})
    
    def _wordBreak(self, s, wordDict, index, memo) -> bool:
        if index in memo:
            return memo[index]
        
        if index == len(s):
            return True
        
        if index > len(s):
            return False
        
        for word in wordDict:
            if s[index:].startswith(word):
                if self._wordBreak(s, wordDict, index + len(word), memo):
                    memo[index] = True
                    return memo[index]
        
        memo[index] = False
        return memo[index]