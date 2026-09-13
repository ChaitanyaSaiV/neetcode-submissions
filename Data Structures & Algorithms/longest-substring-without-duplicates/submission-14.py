class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        result = 0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                result = max(j - i, result)
            else:
                seen.remove(s[i])
                i += 1
        return result