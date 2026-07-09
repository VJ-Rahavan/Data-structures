def find_substring(s):
    
    h = {}
    start = 0
    res = 0
    
    for i in range(len(s)):
        
        if s[i] not in h:
            h[s[i]] = i
        else:
            if h[s[i]] >= start:
                start = h[s[i]] + 1
            h[s[i]] = i
        
        res = max(res, i - start + 1)
    print(res,h)
                
            
find_substring("abcabdcbb")