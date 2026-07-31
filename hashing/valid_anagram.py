# Two strings are anagrams if they have the same character frequencies.
# I count characters in the first string (incrementing) and the second string (decrementing)
# using a single hash map. If every count ends up at 0, they're anagrams.
# Early exit: if the lengths differ, they can't be anagrams.
# Time: O(n), Space: O(k) where k is the alphabet size.

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
