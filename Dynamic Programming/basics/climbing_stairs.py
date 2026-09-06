
# 70. Climbing Stairs (Basic Dynamic Programming)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 1

        for _ in range(2, n + 1):
            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1

# 70. Climbing Stairs (Top-down approach with memoization)
class Solution:
    c = {}
    def climbStairs(self, n: int) -> int:
        if n in self.c:
            return self.c[n]

        if n == 0 or n == 1:
            return 1
        
        val = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.c[n] = val

        return val