# I maintain a fixed-size sliding window equal to the length of s1. 
# As I move the window, I update the frequency map by adding the new character 
# and removing the leftmost character when the window exceeds the required size. 
# Whenever the two frequency maps match, I've found a permutation and return True.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            freq_map = {}
    
            for i in range(len(s1)):
                freq_map[s1[i]] = freq_map.get(s1[i],0) + 1
                
            s2_freq_map = {}
            start = 0

            for i in range(len(s2)):
                s2_freq_map[s2[i]] = s2_freq_map.get(s2[i],0) + 1
        
                while i - start + 1 > len(s1):
                    s2_freq_map[s2[start]] -= 1
                    if s2_freq_map[s2[start]] == 0:
                        del s2_freq_map[s2[start]] 
                    start += 1

                if freq_map == s2_freq_map:
                    return True
            
            return False