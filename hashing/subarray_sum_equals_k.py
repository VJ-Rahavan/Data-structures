# I use the prefix sum + hash map trick.
# As I iterate, I keep a running prefix sum. For each index, if (prefix_sum - k)
# has been seen before, that means there is a subarray ending at the current index
# whose sum equals k. I add the count of such prefix sums to the result.
# I also record the current prefix sum in the map for future lookups.
# Starting the map with {0: 1} handles subarrays that start from index 0.
# Time: O(n), Space: O(n).

def subarray_sum(arr, k):
    prefix_count = {0: 1}
    prefix_sum = 0
    res = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in prefix_count:
            res += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return res


print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 2, 3], 3))
print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))
