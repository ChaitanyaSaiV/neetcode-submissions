class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_map = {}
        result = 0
        for r in range(len(s)):
            if s[r] not in char_map:
                char_map[s[r]] = 1
            else:
                char_map[s[r]] += 1
            
            while (r - l + 1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result