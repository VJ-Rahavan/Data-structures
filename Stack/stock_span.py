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
