def sumArray(arr, idx=0):
    if idx == len(arr):
        return 0

    return arr[idx] + sumArray(arr, idx + 1)