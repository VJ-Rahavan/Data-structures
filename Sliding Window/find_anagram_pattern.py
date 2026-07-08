# Count Anagrams of a Pattern

#My Approach: Not optimized. O(n*klogk) time complexity and O(k) space complexity.
#  Sort the pattern and sort the substring of the string of length equal to the pattern. 
# If they are equal, then it is an anagram. Keep a count of such occurrences.
def find_anagram_pattern(s,pat):
    res = 0
    start = 0
    k = len(pat)
    
    pat_sort = sorted(pat)
    for i in range(len(s)):
        if i >= k-1:
            temp = sorted(s[start:i+1])
            print(temp,pat_sort)
            if temp == pat_sort:
                res+=1
            start += 1
    
    print(res)


find_anagram_pattern("forxxorfxdofr",'for')   