class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        hash_map = {}
        i = 0
        longest = 0
        
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] >= i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j - i + 1)
        
        return longest
