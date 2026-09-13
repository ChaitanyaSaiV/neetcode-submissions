class Solution:
    def findMin(self, nums: List[int]) -> int:
        length_nums = len(nums)
        low = 0
        high = length_nums - 1
        while low <= high:
            if nums[low] <= nums[high]:
                return nums[low]
            mid = low + (high - low) // 2
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == length_nums - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1