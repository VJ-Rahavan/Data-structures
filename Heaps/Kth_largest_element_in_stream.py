# I maintain a min heap of size K containing the K largest elements seen so far. 
# Whenever a new value is added, I push it into the heap. 
# If the heap exceeds size K, I remove the smallest element. 
# Therefore, the smallest element remaining at the root is always the Kth largest.


import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]