# For each encoded number, I extract the last digit as the width, 
# split the remaining digits into base x and exponent y, 
# and calculate x^y mod 1e9+7 using Python's three-argument pow, 
# which performs modular exponentiation efficiently. 
# I accumulate the results modulo 1e9+7 to prevent the sum from growing unnecessarily.

class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 1_000_000_007 # or pow(10, 9) + 7
        res = 0

        for num in nums:
            width = num % 10
            s = str(num // 10)

            x = int(s[:width])
            y = int(s[width:])

            res = (res + pow(x, y, MOD)) % MOD

        return res