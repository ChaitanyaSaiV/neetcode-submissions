class Solution:
    def findMinIndex(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l

    def binarySearch(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def search(self, nums, target):
        if not nums:
            return -1
        minIndex = self.findMinIndex(nums)
        n = len(nums)

        # If target is in the right half
        if nums[minIndex] <= target <= nums[n - 1]:
            return self.binarySearch(nums, minIndex, n - 1, target)
        # Else target is in left half
        else:
            return self.binarySearch(nums, 0, minIndex - 1, target)
