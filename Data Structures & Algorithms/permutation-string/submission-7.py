class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1)])
        l, r = 0, len(s1) - 1
        
        while r < len(s2):
            if s1Counter == s2Counter:
                return True
            r += 1
            if r < len(s2):
                s2Counter[s2[r]] = s2Counter.get(s2[r], 0) + 1
            s2Counter[s2[l]] -= 1
            if s2Counter[s2[l]] == 0:
                del s2Counter[s2[l]]
            l += 1
        
        return False
