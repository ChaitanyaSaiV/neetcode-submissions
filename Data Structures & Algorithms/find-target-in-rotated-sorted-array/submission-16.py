class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMin(nums)
        if target >= nums[minIndex] and target <= nums[len(nums) - 1]:
            l = minIndex
            r = len(nums) - 1
        else:
            l = 0
            r = minIndex - 1
        return self.binarySearch(nums, l, r, target)
    
    def binarySearch(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = l + (r - l)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l