class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] not in alpha_num:
                i += 1
                continue
            if s[j] not in alpha_num:
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True