# I use a hash map that stores each value's index as I scan the array.
# For every number, I compute its complement (target - num) and check if it's already in the map.
# If it is, I've found the pair. Otherwise, I add the current number and its index and continue.
# This gives O(n) time and O(n) space — one pass, single hash lookup per element.

def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
