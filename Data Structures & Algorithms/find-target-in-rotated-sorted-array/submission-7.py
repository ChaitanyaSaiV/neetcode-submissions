class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.finMinIndex(nums)
        print(minIndex)
        targetIndex = self.binarySearch(nums, 0, minIndex - 1, target)
        if targetIndex == -1:
            return self.binarySearch(nums, minIndex, len(nums) - 1, target)
        else:
            return targetIndex

    def finMinIndex(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l
    
    def binarySearch(self, nums, left, right, target) -> int:
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1