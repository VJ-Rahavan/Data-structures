# I'll use a hash map where the key is the sorted version of each string.
# Since all anagrams contain the same characters, sorting them produces the same key.
# For every string, I sort it, use the sorted string as the key, and
#  append the original string to the corresponding list in the hash map. 
# Finally, I return all the grouped values from the hash map.

def group_anagrams(arr):
    freq = {}
    
    for i in arr:
        sorted_string = "".join(sorted(i))
        print(sorted_string,i)
        if sorted_string in freq:
            freq[sorted_string].append(i)
        else:
            freq[sorted_string] = [i]
        
    print(list(freq.values()))

# Instead of sorting every string, 
# I create a frequency array of size 26 to count how many times each lowercase letter appears. 
# Two strings are anagrams if they have the exact same character frequencies. 
# After building the frequency array, I convert it into a tuple so it can be used as a dictionary key. 
# If another string has the same frequency tuple, it belongs to the same anagram group.

#optimized approach
def group_anagrams(arr):
    freq = {}

    for s in arr:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        key = tuple(count)

        if key in freq:
            freq[key].append(s)
        else:
            freq[key] = [s]

    return list(freq.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# For optimizal approach with A - Z
# count = [0] * 52

# for ch in s:
#     if 'A' <= ch <= 'Z':
#         count[ord(ch) - ord('A')] += 1
#     else:
#         count[26 + ord(ch) - ord('a')] += 1