# I maintain a sliding window and a frequency map of fruit types inside the window. 
# Whenever the window contains more than two distinct fruits, 
# I shrink it from the left until only two types remain. 
# At each step, I update the maximum valid window length.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
            freq_map = {}
            start = 0 
            maxx = 0
            
            for i in range(len(fruits)):
                freq_map[fruits[i]] = freq_map.get(fruits[i],0) + 1
                
                while len(freq_map) > 2:
                    freq_map[fruits[start]] -= 1
                    if freq_map[fruits[start]] == 0:
                        del freq_map[fruits[start]]
                    start += 1
                    
                maxx = max(maxx, i - start + 1)
            
            return maxx
        