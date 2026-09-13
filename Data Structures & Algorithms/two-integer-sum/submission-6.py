class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for index, num in enumerate(nums):
            if num in remainders:
                return [remainders[num], index]
            
            remainder = target - num
            remainders[remainder] = index
        return None