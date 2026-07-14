# I use two stacks. The first stack stores all the values. 
# The second stack stores the minimum value corresponding to each position in the main stack. 
# On every push, I compare the new value with the current minimum and push the smaller one onto the min stack. 
# On every pop, I remove the top element from both stacks. 
# This guarantees that push, pop, top, and getMin all run in O(1) time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)

        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))

    def pop(self):
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]