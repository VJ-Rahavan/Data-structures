# I use two stacks to simulate queue operations efficiently. 
# All enqueue operations go into in_stack, and elements are transferred to out_stack only when it is empty. 
# This ensures each element is moved at most once between the stacks, 
# giving O(1) amortized time for enqueue and dequeue operations.

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.transfer()
        print(self.out_stack)
        if self.out_stack:
            return self.out_stack.pop()

    def peek(self) -> int:
        self.transfer()
        if self.out_stack:
            return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
    
    def transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()