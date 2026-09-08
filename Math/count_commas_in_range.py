# n < 10 pow 5
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return n - 999
   
# We count commas position by position instead of checking every number.
# The first comma appears at 1000, so numbers from 1000 to n contribute n - 1000 + 1 commas.
# The next comma starts at 1,000,000, then 1,000,000,000, so we multiply x by 1000 each time.
# We keep adding n - x + 1 while x <= n.
# This gives O(log n) time and O(1) space.
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000

        while x <= n:
            ans += n - x + 1
            x *= 1000

        return ans