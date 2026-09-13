class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self._rob(nums, 0, memo)

    def _rob(self, nums, index, memo) -> int:
        if index in memo:
            return memo[index]
        
        if index >= len(nums):
            return 0
        
        include_first_house = nums[index] + self._rob(nums, index + 2, memo)
        exclude_first_house = self._rob(nums, index + 1, memo)

        memo[index] = max(include_first_house, exclude_first_house)

        return memo[index]
        