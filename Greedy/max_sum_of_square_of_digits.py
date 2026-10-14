
# I use a greedy approach to maximize the sum of squared digits by placing the largest possible digits first. 
# First, I check whether the given digit sum is valid; 
# if it exceeds `num * 9` or is less than `1`, I return an empty string. 
# Then, I repeatedly choose the minimum of `9` and the remaining sum, 
# Append it to the result, and subtract it from the remaining sum. 
# Finally, I join the digits and return the string. 
# The time and space complexities are both O(num).

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9 or sum < 1:
            return ""

        result = []

        for _ in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return "".join(result)
