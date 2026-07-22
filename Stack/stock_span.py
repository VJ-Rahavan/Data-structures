class StockSpanner:

    def __init__(self):
        self.stack = []
        self.arr = []

    def next(self, price: int) -> int:
        
        self.arr.append(price)
        n = len(self.arr)

        while self.stack and self.arr[self.stack[-1]] <= price:
            self.stack.pop()
        
        result = 0
        if self.stack:
            result = n - self.stack[-1] - 1
        else:
            result = n
        
        self.stack.append(n - 1)
        return result

#Optimized version
class StockSpanner:

    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span

# I use a monotonic decreasing stack that stores (price, span) pairs. 
# For each new price, I pop all previous prices that are less than or equal to it and 
# add their stored spans to the current span, since those days are guaranteed to be part of the current answer. 
# Then I push the current (price, span) onto the stack. 
# This ensures each element is pushed and popped at most once, giving an amortized O(1) time complexity.