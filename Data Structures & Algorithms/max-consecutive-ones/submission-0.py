class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append('#')
        i = 0
        count = 0
        for index, num in enumerate(nums):
            if num == 0 or num == '#':
                count = max(count, index - i)
                i = index + 1
        
        return count

            

