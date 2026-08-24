arr= [10, 5, 2, 7, 1, -10]
k = 15
# Output: 6
 # Python program to find longest sub-array having sum k
# using Hash Map and Prefix Sum

# Function to find longest sub-array having sum k
def longestSubarray(arr, k):
    mp = {}
    res = 0
    prefSum = 0

    for i in range(len(arr)):
        prefSum += arr[i]

        # Check if the entire prefix sums to k
        if prefSum == k:
            res = i + 1

        # If prefixSum - k exists in the map then there exist such 
      	# subarray from (index of previous prefix + 1) to i.
        elif (prefSum - k) in mp:
            print(i,mp[prefSum - k])
            res = max(res, i - mp[prefSum - k])

        # Store only first occurrence index of prefSum
        if prefSum not in mp:
            mp[prefSum] = i
        
        # print(i,arr[i])

    return res

print(longestSubarray(arr, k))