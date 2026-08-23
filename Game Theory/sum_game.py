# * Count the known digit sums and `?` counts in both halves.
# * If the total number of `?` is odd, Alice wins because she gets the final move.
# * Otherwise, Bob can win only if the existing sum difference can be exactly balanced by the `?` difference.
# * Each `?` contributes up to `9`, so compare `first_sum - second_sum` with `9 * (second_q - first_q) // 2`.



class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        first_q = 0
        first_sum = 0

        for i in range(half):
            if num[i] == '?':
                first_q += 1
            else:
                first_sum += int(num[i])

        second_q = 0
        second_sum = 0

        for i in range(half, n):
            if num[i] == '?':
                second_q += 1
            else:
                second_sum += int(num[i])

        if (first_q + second_q) % 2 == 1:
            return True

        return first_sum - second_sum != 9 * (second_q - first_q) // 2