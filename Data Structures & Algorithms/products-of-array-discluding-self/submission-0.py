class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = 1
        for num in nums:
            product *= num
            prefix.append(product)
        
        reversed_nums = nums[::-1]
        postfix = [1]
        product = 1
        for num in reversed_nums:
            product *= num
            postfix.append(product)
        
        postfix = postfix[::-1]

        result = []

        for index in range(1, len(nums)+1):
            result.append(prefix[index-1] * postfix[index])

        
        return result