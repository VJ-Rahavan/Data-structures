# I use a Max Heap because I repeatedly need the two largest stones. 
# Since Python provides a Min Heap, I store negative values. I remove the two largest stones, and if they differ, I push their difference back. The remaining stone is the answer.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0