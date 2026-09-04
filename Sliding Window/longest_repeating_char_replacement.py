# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.


#Approach: Sliding Window
# I expand the window and track character frequencies. 
# If the window size minus the highest character frequency is greater than k,
#  I shrink from the left. For every valid window, I update the maximum length.

# I'll use a sliding window. 
# As I expand the window, I'll maintain the frequency of each character and track the maximum frequency of any character seen in the window.
# If the number of characters that need replacement, which is (window_size - max_freq), 
# If it exceeds k, I'll shrink the window from the left.
# After every valid window, I'll update the maximum length.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxx = 0
        start = 0
        max_freq = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

            max_freq = max(max_freq, seen[s[i]])

            while i - start + 1 - max_freq > k:
                seen[s[start]] -= 1
                start += 1

            maxx = max(maxx, i - start + 1)

        return maxx
