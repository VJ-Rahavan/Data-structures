# Input: arr[] = [3, 1, 2, 2, 2, 2]
# Output: 5

# Longest subarray length with atmost two distinct integers

def find_longest(arr):
    start = 0
    seen = {}
    cur = 0
    maxx = 0

    for i in range(len(arr)):
        seen[arr[i]] = seen.get(arr[i],0) + 1

        while len(seen) > 2:
            seen[arr[start]] -= 1
            
            if seen[arr[start]] == 0:
                del seen[arr[start]]
            start += 1

        maxx = max(maxx,i - start + 1)
    
    print(maxx)


find_longest([3, 1, 2, 2, 2, 2])