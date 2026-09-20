

from bisect import bisect_left

class Solution:
    def countIntersectionPairs(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ends = sorted(end for _, end in intervals)

        non_intersecting = 0

        for start, _ in intervals:
            non_intersecting += bisect_left(ends, start)

        total_pairs = n * (n - 1) // 2
        return total_pairs - non_intersecting



class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        active = []
        count = 0

        import heapq

        for start, end in intervals:
            while active and active[0] < start:
                heapq.heappop(active)

            count += len(active)
            heapq.heappush(active, end)

        return count



