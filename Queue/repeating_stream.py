from collections import deque

#my approach is to use a deque to keep track of the characters in the stream.
# I also use a hash map to count the occurrences of each character.
# For each character in the stream, I increment its count in the hash map.
# If the count of the character is greater than 1, I remove characters from the front of the deque until I find a character with a count of 1.
# If the deque is empty, it means there are no non-repeating characters, so I append '#' to the result string. Otherwise, 
# I append the character at the front of the deque to
def repeating_stream(arr):
    q = deque()
    res = ""
    h = {}
    for i in arr:
        h[i] = h.get(i,0) + 1
        # print(i,h,)
        if h and h[i] > 1:
            while q and h[q[0]] > 1:
                q.popleft()
            if q:
                res += q[0]
            else:
                res += "#"
                
            print(h,i,res)
        else:
            q.append(i)
            res += q[0]
    print(res)

# Given example
repeating_stream("aabc")      # a#bb
# Single character
repeating_stream("a")         # a
# All unique
repeating_stream("abcd")      # aaaa
# All same
repeating_stream("aaaa")      # a###
# First non-repeating changes multiple times
repeating_stream("aabcdbe")   # a#bbbcc
# Eventually no non-repeating characters
repeating_stream("aabba")     # a#b##
# Another transition
repeating_stream("abcabc")    # aaabc#
# New unique appears after repeats
repeating_stream("aabccd")    # a#bbbb
# Repeating later
repeating_stream("abac")      # aabb
# Empty string
repeating_stream("")          # ""
# Longer mixed case
repeating_stream("geeksforgeeks")

# Alternate approach:
# I use a deque to maintain the order of characters and a hash map to count their occurrences.
# For each character in the stream, I increment its count in the hash map.
# If the count of the character is greater than 1, I remove characters from the front of the deque until I find a character with a count of 1.
# If the deque is empty, it means there are no non-repeating characters, so I append '#' to the result string

from collections import deque

def repeating_stream(s):
    freq = {}
    q = deque()
    res = ""

    for ch in s:
        # Count frequency
        freq[ch] = freq.get(ch, 0) + 1

        # Add current character
        q.append(ch)

        # Remove all repeating characters from the front
        while q and freq[q[0]] > 1:
            q.popleft()

        # First non-repeating character
        if q:
            res += q[0]
        else:
            res += "#"

    return res