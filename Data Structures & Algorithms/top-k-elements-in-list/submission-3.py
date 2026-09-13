import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_counter = Counter(nums)
        for num in num_counter:
            heapq.heappush(heap, (num_counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result