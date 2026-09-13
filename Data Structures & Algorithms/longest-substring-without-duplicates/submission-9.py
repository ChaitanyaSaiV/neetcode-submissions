class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        l, r = 0, 0
        count = 0
        while r <= len(s) - 1:
            if s[r] in sSet:
                while s[r] in sSet:
                    sSet.remove(s[l])
                    l += 1
            sSet.add(s[r])
            count = max(count, (r - l + 1))
            r += 1
        
        return count
            
