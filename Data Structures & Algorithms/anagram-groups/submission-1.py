class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in hash_map:
                hash_map[key] = []

            hash_map[key].append(word)
        result = []
        for anagram in hash_map:
            result.append(hash_map[anagram])
        
        return result