class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set(nums)

        return len(nums) != len(counter)