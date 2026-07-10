# I use a sliding window with two pointers.
#  I expand the window by moving the right pointer and 
# adding the current element to the running sum. 
# If the sum exceeds the target, 
# I shrink the window from the left until the sum becomes valid again. 
# Once the window is valid, I calculate its length and update the maximum length found so far.


def find_atmost_k_arr(arr,k):
    start = 0
    cur = 0
    res = float("-inf")
    for i in range(len(arr)):
        cur += arr[i]
        while cur > k:
            print(i,start)
            cur -= arr[start]
            start += 1
        res = max(res,i - start + 1)
    print(res)

find_atmost_k_arr([1, 2, 1, 0, 1, 1, 0],4)