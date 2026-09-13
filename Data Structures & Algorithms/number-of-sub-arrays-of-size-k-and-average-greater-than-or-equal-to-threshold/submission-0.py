class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l , r = 0, k - 1
        subArraySum = 0
        res = 0
        for num in arr[l:r + 1]:
            subArraySum += num
        
        if (subArraySum / k) >= threshold:
            res += 1
        
        while r < len(arr) - 1:
            r += 1
            subArraySum += arr[r]
            subArraySum -= arr[l]
            l += 1
            print(subArraySum)
            if (subArraySum / k) >= threshold:
                res += 1
        
        return res