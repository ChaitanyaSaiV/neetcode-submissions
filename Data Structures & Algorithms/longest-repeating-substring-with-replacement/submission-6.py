class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        l = 0
        sMap = {}
        
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            
            # Check if current window is valid
            while (r - l + 1) - max(sMap.values()) > k:
                sMap[s[l]] -= 1
                l += 1
            
            # Update max count with current window length
            count = max(count, r - l + 1)
        
        return count

        
