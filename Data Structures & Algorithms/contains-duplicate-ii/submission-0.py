class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for index, num in enumerate(nums):
            if num in hashMap:
                if abs(index - hashMap[num]) <= k:
                    return True
                else:
                    hashMap[num] = index
            else:
                hashMap[num] = index
        
        return False
