class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = float("-inf")
        memo = {}
        for index in range(len(nums)):
            current_count = self._lengthOfLIS(nums, index, memo)
            count = max(current_count, count)
        return count

    def _lengthOfLIS(self, nums, index, memo):
        if index in memo:
            return memo[index]
        if index == len(nums):
            return 0
        count = 1
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index]:
                current_count = 1 + self._lengthOfLIS(nums, i, memo)
                count = max(current_count, count)
        memo[index] = count
        return memo[index]