class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        hashMap = Counter(blocks[l:r + 1])
        count = hashMap['W']
        while r < len(blocks) - 1:
            r += 1
            hashMap[blocks[r]] += 1
            hashMap[blocks[l]] -= 1
            l += 1
            if hashMap['W'] < count:
                count = hashMap['W']
        
        return count