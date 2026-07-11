# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.


#Approach: Sliding Window
# I expand the window and track character frequencies. 
# If the window size minus the highest character frequency is greater than k,
#  I shrink from the left. For every valid window, I update the maximum length.

def find_longest(arr,k):
    freq = {}
    
    start = 0
    n = len(arr)
    res = 0
    
    for i in range(n):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        
        window_size = i - start + 1
        max_freq = max(freq.values())

        while window_size - max_freq > k:
                freq[arr[start]] -= 1
                start += 1
                
        res = max(res, i - start + 1)
        
    print(freq, res)
    
    
    
find_longest("ABAB",2)    