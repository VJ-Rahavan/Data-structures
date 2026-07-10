#Minimum Size Subarray Sum

def find_min_sum_arr(arr,target):
    start = 0
    cur = 0
    res = float("inf")
    for i in range(len(arr)):
        cur += arr[i]
        while cur >= target:
            res = min (res,i - start + 1)
            cur -= arr[start]
            start += 1
    print(0 if res == float("inf") else res)

find_min_sum_arr([2,3,1,2,4,3],7)