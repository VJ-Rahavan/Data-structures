# I compute the answer in two passes without using division.
# First pass builds a prefix product: res[i] = product of all elements to the left of i.
# Second pass multiplies each res[i] by the running suffix product (all elements to the right of i).
# This gives O(n) time and O(1) extra space (output array not counted).

def product_except_self(arr):
    n = len(arr)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
