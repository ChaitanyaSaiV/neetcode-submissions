class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0

        for num in nums:
            previous_num = num - 1
            if previous_num not in num_set:
                current_length = 0
                current = num
                while current in num_set:
                    current_length += 1
                    current += 1
                
                longest = max(longest, current_length)
        
        return longest