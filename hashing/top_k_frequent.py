# I use bucket sort to get O(n) time.
# First I build a frequency map counting occurrences of each element.
# Then I create buckets where bucket[i] holds all elements that appear exactly i times.
# Finally, I walk the buckets from highest frequency down and collect the first k elements.
# This avoids sorting (O(n log n)) and heap-based approaches (O(n log k)).

def top_k_frequent(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(arr) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    res = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

    return res


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))
