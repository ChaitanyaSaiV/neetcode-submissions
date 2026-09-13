class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        hashMap = Counter(blocks[l:r + 1])
        print(blocks[l:r])
        count = hashMap['W']
        while r < len(blocks) - 1:
            print(hashMap)
            if hashMap['W'] < count:
                count = hashMap['W']
            
            r += 1
            hashMap[blocks[r]] += 1
            hashMap[blocks[l]] -= 1
            l += 1

        return count