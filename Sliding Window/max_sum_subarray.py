#Maximum sum subarray of size K

def max_sum_subarray(arr,k):
    if len(arr) < k:
        return None  # or raise ValueError
    cur = sum(arr[:k])
    res = cur
    for i in range(k,len(arr)):
        cur = cur - arr[i - k] + arr[i]
        res = max(cur,res)
    
    print(res)
    
max_sum_subarray([2,3,5,6,7],2)