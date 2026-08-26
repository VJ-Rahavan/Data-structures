# I use a sliding window with two pointers and maintain the number of 1s using count.
# I shrink the window when there are more than k ones or when there are unnecessary leading zeros.
# When the window contains exactly k ones, I compare it with best based on length and then lexicographical order.
# The pointer movement is O(n), but because of substring creation/comparison, the worst-case time is O(n²) and space is O(n).

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        left = 0
        count = 0
        best = ""

        for right in range(n):

            if s[right] == "1":
                count += 1

            # Shrink while over budget, or while leading char is a
            # useless zero (only safe to also strip zeros once we're
            # at or under k, but zeros never affect count anyway)

            while count > k or s[left] == "0":
                if s[left] == "1":
                    count -= 1
                left += 1

            if count == k:
                candidate = s[left:right + 1]

                if (not best or
                    len(candidate) < len(best) or
                    (len(candidate) == len(best) and candidate < best)):
                    best = candidate

        return best


#Optimal approach
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == "1"]

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            curr = s[ones[i]:ones[i + k - 1] + 1]

            if not ans or len(curr) < len(ans) or \
               (len(curr) == len(ans) and curr < ans):
                ans = curr

        return ans