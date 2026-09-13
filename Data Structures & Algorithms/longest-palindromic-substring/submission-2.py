class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        length = 0

        for i in range(len(s)):
            # odd
            low, high = i, i
            while low >= 0 and high <= len(s) - 1 and s[low] == s[high]:
                if high - low + 1 > length:
                    length = high - low + 1
                    result = s[low : high + 1]
                
                low -= 1
                high += 1
            
            low = i
            high = i + 1

            while low >= 0 and high <= len(s) - 1 and s[low] == s[high]:
                if high - low + 1 > length:
                    length = high - low + 1
                    result = s[low : high + 1]
                
                low -= 1
                high += 1
        
        return result
        