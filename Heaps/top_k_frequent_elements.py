import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for i in freq:
            heapq.heappush(heap, (freq[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x for y, x in heap]
