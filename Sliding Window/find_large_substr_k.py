# I use a sliding window and a frequency map to track characters in the current window.
# If the number of distinct characters exceeds K, 
# I shrink the window from the left until it becomes valid again.
# For every valid window, I update the maximum length using i - start + 1

def find_large_substring(s,k):
    
    start = 0
    freq = {}
    res = 0
    
    for i in range(len(s)):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
        
        while len(freq) > k:
            freq[s[start]] -= 1
            
            if freq[s[start]] == 0:
                del freq[s[start]]
            
            start += 1
        
        res = max(res,i - start + 1)
    print(res)

find_large_substring("abbbbbbc",2)