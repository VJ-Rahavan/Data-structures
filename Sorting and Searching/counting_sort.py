# Counting Sort counts the frequency of each value using an auxiliary array and then reconstructs the sorted array by outputting each value according to its frequency.

def counting_sort(arr):
    
    largest_number = max(arr)
    
    counting_arr = [0] * (largest_number + 1)
    
    for i in arr:
        counting_arr[i] += 1
    
    res = []
    
    for i in range(len(counting_arr)):
        if counting_arr[i] > 0:
            d = [i] * counting_arr[i]
            res.extend(d)
    
    print(res)
