class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l, r = 0, k

        while r <= len(nums):
            maximum = float("-inf")
            for i in range(k):
                maximum = max(maximum, nums[l+i])
            result.append(maximum)
            l += 1
            r += 1
        
        return result