class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        length = len(nums)
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
            if hashMap[num] > length / 2:
                return num
        return  