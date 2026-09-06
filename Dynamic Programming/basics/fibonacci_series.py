# 509. Fibonacci Number (Top-down approach)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
# Output: 5

# 509. Fibonacci Number (Bottom-up approach)
def fibonacci_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

print(fibonacci_bottom_up(5))
# Output: 5

# 509. Fibonacci Number (Space optimized approach)
def fibonacci_space_optimized(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

print(fibonacci_space_optimized(5))
# Output: 5