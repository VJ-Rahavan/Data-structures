def exponent_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1

    # Find the possible range
    while i < len(arr) and arr[i] <= target:
        i *= 2

    start = i // 2
    end = min(i, len(arr) - 1)

    # Binary Search
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1