class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1)])
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if s1Counter == s2Counter:
                return True
            else:
                r += 1
                if r < len(s2):
                    if s2[r] in s2Counter:
                        s2Counter[s2[r]] += 1
                    else:
                        s2Counter[s2[r]] = 1
                
                s2Counter[s2[l]] -= 1
                if s2Counter[s2[l]] <= 0:
                    del s2Counter[s2[l]]
                l += 1
        return False