# Radix Sort sorts numbers digit by digit, from the least significant digit to the most significant digit, using a stable Counting Sort at each digit.

def radix_sort(arr):
    
    largest_number = max(arr)
    
    # print(number_len)
    exp = 1
    while largest_number//exp > 0:
        bucket = [[] for _ in range(10)]
        # print(bucket)
        for i in range(len(arr)):
            r = (arr[i] // exp ) % 10
            print(arr[i],r)
            bucket[r].append(arr[i])
        arr=[]
        for i in bucket:
            arr.extend(i)
        exp *= 10
    
    print(arr)
        
radix_sort([37,3,100,1,2])
    





# I would separate the array into negative and non-negative numbers. I'd convert the negative values to their absolute values, sort both arrays independently using Radix Sort, convert the negatives back, reverse their order, and finally concatenate the negative array with the positive array.