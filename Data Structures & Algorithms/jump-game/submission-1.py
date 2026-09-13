class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self._canJump(nums, 0, {})
    def _canJump(self, nums: List[int], index, memo) -> bool:
        if index in memo:
            return memo[index]
        
        if index >= len(nums) - 1:
            return True
        
        for i in range(1, nums[index] + 1):
            if self._canJump(nums, index + i, memo):
                memo[index] = True
                return True
        
        memo[index] = False

        return memo[index]
        