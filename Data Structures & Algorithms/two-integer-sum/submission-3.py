class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        index = 0
        for num in nums:
            remainder = target - num
            if remainder in hashMap:
                return [hashMap[remainder], index]
            
            hashMap[num] = index
            index += 1
        return [0,0]
