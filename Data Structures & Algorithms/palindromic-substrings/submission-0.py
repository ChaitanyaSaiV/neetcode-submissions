class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []

        for i in range(len(s)):
            #odd
            low = i
            high = i
            while low >= 0 and high <= len(s) - 1 and s[low] == s[high]:
                result.append(s[low:high+1])
                low -= 1
                high += 1
            
            low = i
            high = i + 1
            while low >= 0 and high <= len(s) - 1 and s[low] == s[high]:
                result.append(s[low:high+1])

                low -= 1
                high += 1
        
        return len(result)