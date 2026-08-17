# I extract the last digit using modulo 10 
# and build the reversed number by multiplying the current result by 10 and adding the digit. 
# Before adding each digit, I check whether the result would exceed the 32-bit signed integer limit. 
# If it would overflow, I return 0; otherwise, I return the result with its original sign.

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            if result > (2**31 - 1 - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result