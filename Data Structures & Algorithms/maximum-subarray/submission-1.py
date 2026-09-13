class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        current_sum = 0
        i = 0
        while i < len(nums):
            current_sum += nums[i]
            if current_sum > maxsum:
                maxsum = current_sum
                
            if current_sum < 0:
                current_sum = 0
            
            i += 1

        return maxsum

