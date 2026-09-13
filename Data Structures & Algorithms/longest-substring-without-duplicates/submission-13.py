class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_length = 0
        string_set = set()
        while j < len(s):
            if s[j] not in string_set:
                string_set.add(s[j])
                j += 1
                max_length = max(max_length, len(string_set))
                continue

            while s[j] in string_set:
                string_set.remove(s[i])
                i += 1
        
        return max_length