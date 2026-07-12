# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]

def find_all_anagrams(s,p):
    
    res = []
    
    start = 0
    
    freq_map = {}
    
    for i in p:
        freq_map[i] = freq_map.get(i,0) + 1
    
    freq_map2 = {}
    
    for i in range(len(s)):
        freq_map2[s[i]] = freq_map2.get(s[i],0) + 1
        
        while i - start + 1 > len(p):
            freq_map2[s[start]] -= 1
            
            if freq_map2[s[start]] == 0:
                del freq_map2[s[start]]
            
            start += 1
        # print(freq_map2,freq_map)
        if freq_map == freq_map2:
            res.append(start)
        
    print(res)

find_all_anagrams("cbaebabacd","abc")
        