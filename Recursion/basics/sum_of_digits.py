
#First time alone convert negative to positive and then find sum of digits of n using recursion
def sumOfDigits(n):
    if n < 0:
        n = -n

    if n == 0:
        return 0

    r = n % 10

    return r + sumOfDigits(n // 10)

print(sumOfDigits(-123))  # 6