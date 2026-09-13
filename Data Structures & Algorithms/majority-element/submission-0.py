class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = float("-inf")
        result = None
        for num in counter:
            if counter[num] > majority:
                result = num
                majority = counter[num]
        
        return result