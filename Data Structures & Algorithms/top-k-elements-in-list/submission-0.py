import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        
        result = []

        for num in hashmap:
            heapq.heappush(result, (hashmap[num], num))
            if len(result) > k:
                heapq.heappop(result)
        
        second_result = []

        for element in result:
            a, b = element
            second_result.append(b)

        return second_result
