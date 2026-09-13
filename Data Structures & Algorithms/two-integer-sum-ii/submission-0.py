class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum2 = numbers[l] + numbers[r]
            if sum2 == target:
                return [l + 1, r + 1]
            
            if sum2 > target:
                r -= 1
            else:
                l += 1
        
        return