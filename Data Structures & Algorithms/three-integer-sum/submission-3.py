class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1
            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]
                if current_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < len(nums) and nums[low] == nums[low - 1]:
                        low += 1
                    while high > 0 and nums[high] == nums[high + 1]:
                        high -= 1
                elif current_sum < 0:
                    low += 1
                else:
                    high -= 1
        return result

            