class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_count = 1
                current_num = num + 1
                while current_num in nums_set:
                    current_count += 1
                    current_num += 1
                
                count = max(count, current_count)
        
        return count