from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.window:
            self.total -= self.queue.popleft()

        return self.total / len(self.queue)