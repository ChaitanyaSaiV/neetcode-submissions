class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[1:], 0, {}), self._rob(nums[:-1], 0, {}))

    def _rob(self, nums, index, memo) -> int:
        if index in memo:
            return memo[index]
        
        if index >= len(nums):
            return 0
        
        include_first_house = nums[index] + self._rob(nums, index + 2, memo)
        exclude_first_house = self._rob(nums, index + 1, memo)

        memo[index] = max(include_first_house, exclude_first_house)

        return memo[index]
        
        