# Since timestamps are strictly increasing, expired requests are always at the front of the queue. 
# I append the new timestamp, remove expired timestamps from the front until the oldest one is within the last 3000 ms, 
# and then return the queue size. Each timestamp is added once and removed once, 
# so the amortized time complexity is O(1).

from collections import deque 

class RecentCounter:

    def __init__(self):
        self.arr = deque()

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr[0] < t - 3000:
            self.arr.popleft()
        
        return len(self.arr)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)