class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        return len(nums) != len(counter)