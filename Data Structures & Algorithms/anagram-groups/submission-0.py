from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        res = []
        for string in strs:
            key = ''.join(sorted(string))
            if key in anagrams_map:
                anagrams_map[key].append(string)
            else:
                anagrams_map[key] = [string]

        for anagrams in anagrams_map:
            res.append(anagrams_map[anagrams])
        
        return res