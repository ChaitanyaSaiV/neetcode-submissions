import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counts = Counter(nums)
        heap = []
        for num in frequency_counts:
            heapq.heappush(heap, (-(frequency_counts[num]), num))
        
        i = 0
        result = []
        while i != k:
            result.append(heapq.heappop(heap)[1])
            i += 1
        return result