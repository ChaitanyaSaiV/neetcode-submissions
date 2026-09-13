class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        product = 1
        for num in nums:
            product *= num
            prefix_product.append(product)
        
        postfix_product = [1]
        product = 1
        reversed_nums = nums[::-1]
        for num in reversed_nums:
            product *= num
            postfix_product.append(product)
        postfix_product = postfix_product[::-1]
        result = []
        i = 0
        j = 1
        while j < len(postfix_product):
            result.append(prefix_product[i] * postfix_product[j])
            i += 1
            j += 1
        return result
