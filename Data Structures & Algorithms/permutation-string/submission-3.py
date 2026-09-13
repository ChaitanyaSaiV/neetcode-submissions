
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        window = Counter()

        for i in range(len2):
            window[s2[i]] += 1
            # Shrink window if its size > len1
            if i >= len1:
                left_char = s2[i - len1]
                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1

            if window == count_s1:
                return True

        return False
