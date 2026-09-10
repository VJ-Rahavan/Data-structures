def maxNum(arr, maxx, idx=1):
    if idx == len(arr):
        return maxx

    return maxNum(arr, max(maxx, arr[idx]), idx + 1)

inp = [2, 6, 3, 1]
print(maxNum(inp, inp[0]))