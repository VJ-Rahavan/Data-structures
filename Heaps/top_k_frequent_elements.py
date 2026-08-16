# I first build a frequency map for every number. 
# Then I iterate through the map and maintain a Min Heap of size K, 
# where each entry contains the frequency and number. 
# Whenever the heap exceeds K elements, I remove the element with the lowest frequency. 
# At the end, the heap contains the K most frequent elements.

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
