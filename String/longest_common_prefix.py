# I start with the first string as the initial prefix. 
# Then, for every other string, I compare its characters with the current prefix 
# until they differ or one string ends. I then shorten the prefix to the matching portion. 
# If the prefix becomes empty, I return immediately because no common prefix exists.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            j = 0

            while j < len(prefix) and j < len(s) and prefix[j] == s[j]:
                j += 1

            prefix = prefix[:j]

            if not prefix:
                return ""

        return prefix