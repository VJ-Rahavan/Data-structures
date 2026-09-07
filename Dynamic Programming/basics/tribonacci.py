class Solution:
    def __init__(self):
        self.seen = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        if n in self.seen:
            return self.seen[n]

        val = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        self.seen[n] = val

        return val

#Optimal solution with base cases stored in a dictionary to avoid recomputation. 
# The function recursively computes the tribonacci number for n by 
# summing the tribonacci numbers for n-1, n-2, and n-3, 
# storing results in the seen dictionary for future reference.
class Solution:
    def __init__(self):
        self.seen = {
            0: 0,
            1: 1,
            2: 1
        }

    def tribonacci(self, n: int) -> int:
        if n in self.seen:
            return self.seen[n]

        val = (
            self.tribonacci(n - 1)
            + self.tribonacci(n - 2)
            + self.tribonacci(n - 3)
        )

        self.seen[n] = val
        return val