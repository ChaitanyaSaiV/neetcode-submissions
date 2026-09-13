class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        count = 0
        while r < len(s):
            if s[r] in seen:
                count = max(count, r - l)
                while s[l]!= s[r]:   # Remove until we remove the repeated char
                    seen.remove(s[l])
                    l += 1
                # Remove the repeated char at l too, then move left pointer
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
        
        # Check last substring length after loop finishes
        count = max(count, r - l)
        return count

