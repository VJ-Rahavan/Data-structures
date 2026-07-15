# I implemented a stack using a single queue. 
# The key idea is that after every insertion,
#  I rotate the queue so the newly inserted element moves to the front. 
# This ensures the front of the queue always represents the top of the stack. 
# As a result, pop() and top() become straightforward front-queue operations, 
# while push() takes O(n) because of the rotation.

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q