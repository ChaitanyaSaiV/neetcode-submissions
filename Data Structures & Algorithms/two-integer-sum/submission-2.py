class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in visited:
                return [visited[compliment], i]
            
            visited[num] = i
        return
        