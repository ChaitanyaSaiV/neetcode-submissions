class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = set(s1)
        for index, char in enumerate(s2):
            if char in s1Set:
                print(char)
                if Counter(s2[index:(index+len(s1))]) == Counter(s1):
                    return True

        return False