# I use a sliding window with a frequency map. 
# I expand the right pointer and track character counts. 
# If the window contains more than two distinct characters, 
# I shrink it from the left until it becomes valid again. 
# After each valid window, I update the maximum length.

# Longest Substring with At Most 2 Distinct Characters

def find_long_dist(s):
    freq = {}
    start = 0
    res = 0

    for i in range(len(s)):

        # Add current character to the window
        freq[s[i]] = freq.get(s[i], 0) + 1

        # Shrink window until it has at most 2 distinct characters
        while len(freq) > 2:
            freq[s[start]] -= 1

            if freq[s[start]] == 0:
                del freq[s[start]]

            start += 1

        # Update maximum valid window length
        res = max(res, i - start + 1)

    return res


s = "geeksforgeeks"
print(find_long_dist(s))

