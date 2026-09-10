def isSorted(arr, prev, idx=1):
    if idx == len(arr):
        return True

    if prev > arr[idx]:
        return False

    return isSorted(arr, arr[idx], idx + 1)