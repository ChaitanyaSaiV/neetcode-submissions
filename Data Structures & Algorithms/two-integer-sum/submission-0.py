class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        i = 0

        for num in nums:
            if num in hashmap:
                return [hashmap[num], i]
            
            compliment = target - num

            hashmap[compliment] = i

            i += 1

        