def max_avg_arr(arr, k):
    n = len(arr)
    cur = 0
    res = float("-inf")

    for i in range(n):
        cur += arr[i]

        if i >= k:
            cur -= arr[i - k]

        if i >= k - 1:
            res = max(res, cur / k)

    print(res)