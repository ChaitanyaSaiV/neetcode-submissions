class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashMap = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in hashMap:
                hashMap[key] = []
            
            hashMap[key].append(word)

        for words in hashMap:
            result.append(hashMap[words])

        return result