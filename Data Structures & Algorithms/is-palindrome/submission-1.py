class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True
            
        alpha_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] not in alpha_chars:
                i += 1

            if s[j] not in alpha_chars:
                j -= 1

            if s[i] in alpha_chars and s[j] in alpha_chars:
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1
            
        return True