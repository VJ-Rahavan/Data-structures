# To rotate the array right by k steps, I use the reverse trick.
# First I normalize k with k % n in case k > n.
# Then I reverse the whole array, reverse the first k elements, and reverse the rest.
# This shifts each element to its final position in O(n) time and O(1) extra space.

def rotate(arr, k):
    n = len(arr)
    k = k % n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))
