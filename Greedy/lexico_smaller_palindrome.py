from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)

        if n == 1:
            return s if s > target else ""

        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_count = 0
        mid = '#'

        for i in range(26):
            if cnt[i] % 2:
                odd_count += 1
                mid = chr(97 + i)

            if odd_count > 1:
                return ""

        half = [x // 2 for x in cnt]
        H = n // 2

        def make_palindrome(left):
            if mid != '#':
                return left + mid + left[::-1]
            return left + left[::-1]

        prefix = ""

        for i in range(H):

            for j in range(26):

                if half[j] == 0:
                    continue

                half[j] -= 1

                cur = prefix + chr(97 + j)

                # Largest possible completion
                remaining = ""

                for k in range(25, -1, -1):
                    remaining += chr(97 + k) * half[k]

                candidate_left = cur + remaining
                candidate = make_palindrome(candidate_left)

                if candidate > target:
                    prefix = cur
                    break

                half[j] += 1

            else:
                return ""

        return make_palindrome(prefix)

# One correction from my earlier explanation: **your current implementation is O(n²), not O(n)**, because for every position/candidate you build a remaining string of up to `n` characters. With a fixed alphabet of 26, it's `O(26 · n²) = O(n²)`.

# ---

# # 1. Interview explanation

# You can say this:

# > **First, I observe that a palindrome is completely determined by its first half and, for odd length, its middle character.**
# >
# > So I count the characters in `s`. If more than one character has an odd frequency, it's impossible to form a palindrome.
# >
# > Then I take half of every character's frequency to get the characters available for the first half.
# >
# > Now the problem becomes: **construct the lexicographically smallest first half that can produce a palindrome strictly greater than `target`.**
# >
# > I build this first half from left to right. At every position, I try the available characters from `'a'` to `'z'`.
# >
# > For each candidate character, I temporarily place it and ask whether this prefix can still lead to a valid answer.
# >
# > To check feasibility, I construct the **largest possible completion** of the remaining characters by placing them in descending order. If even this largest possible palindrome is not greater than `target`, then no other completion can work, so I reject that character.
# >
# > Otherwise, I accept the character because I'm trying characters in increasing order, so this is the smallest character that can lead to a valid answer.
# >
# > I repeat this for every position and finally mirror the constructed first half to obtain the palindrome.

# That's a strong interview answer.

# ---

# # 2. Why is the greedy choice correct?

# This is the most important part if the interviewer asks:

# > **"Why can you greedily choose the first feasible character?"**

# Say:

# > At each position, I try characters in increasing order. If a smaller character cannot possibly produce a palindrome greater than the target, I can safely discard it.
# >
# > I determine that using the largest possible completion of the remaining characters. If even that maximum completion is not greater than the target, then every other completion will also be smaller or equal to the target.
# >
# > Therefore, the first character that passes the feasibility check is the smallest character that can participate in a valid solution.

# That's the core proof.

# ---

# # 3. Why descending order in `isPossible`?

# Your code does:

# ```python
# for i in range(25, -1, -1):
#     while freq[i]:
#         cur += chr(ord('a') + i)
# ```

# This deserves an explanation.

# Suppose we've chosen:

# ```text
# prefix = "ab"
# ```

# and remaining characters are:

# ```text
# c, c, d, e
# ```

# We want to know:

# > Can **any** completion make the palindrome greater than target?

# The best possible completion is:

# ```text
# edcc
# ```

# because it's the largest lexicographically.

# So:

# ```text
# prefix + largest_remaining
# ```

# gives us the **maximum possible palindrome** for this prefix.

# If that maximum is:

# ```text
# <= target
# ```

# then we're done:

# ```text
# No completion can work.
# ```

# That's why this is a feasibility check.

# ---

# # 4. Example you can explain in the interview

# Use:

# ```text
# s      = "aabb"
# target = "baaa"
# ```

# ### Step 1 — Frequency

# ```text
# a: 2
# b: 2
# ```

# No odd frequency.

# Therefore palindrome is possible.

# Half:

# ```text
# a: 1
# b: 1
# ```

# So we need to construct:

# ```text
# first_half = ??
# ```

# ---

# ### Step 2 — Try first character

# We try `'a'` first.

# ```text
# prefix = "a"
# remaining = "b"
# ```

# The largest completion is:

# ```text
# "ab"
# ```

# Palindrome:

# ```text
# abba
# ```

# Compare:

# ```text
# abba
# baaa
# ```

# Since:

# ```text
# a < b
# ```

# we know:

# ```text
# abba < baaa
# ```

# And because `abba` is the **largest palindrome possible with prefix `"a"`**, no palindrome beginning with `"a"` can work.

# Therefore:

# ```text
# 'a' → reject
# ```

# ---

# ### Step 3 — Try `'b'`

# ```text
# prefix = "b"
# remaining = "a"
# ```

# Largest completion:

# ```text
# "ba"
# ```

# Palindrome:

# ```text
# baab
# ```

# Compare:

# ```text
# baab
# baaa
#    ↑
#    b > a
# ```

# Therefore:

# ```text
# baab > baaa
# ```

# So `'b'` is feasible.

# Because we tried `'a'` first and it failed, `'b'` is the **smallest feasible choice**.

# We lock it:

# ```text
# prefix = "b"
# ```

# Then the remaining character is `a`.

# Final first half:

# ```text
# "ba"
# ```

# Mirror:

# ```text
# ba + ab
# ↓
# baab
# ```

# Answer:

# ```text
# "baab"
# ```

# ---

# # 5. Your complete flow chart

# ```text
#                     ┌──────────────────┐
#                     │      Start       │
#                     └────────┬─────────┘
#                              │
#                              ▼
#                     ┌──────────────────┐
#                     │ Count characters │
#                     │      in s        │
#                     └────────┬─────────┘
#                              │
#                              ▼
#                  ┌─────────────────────────┐
#                  │ More than 1 odd count?  │
#                  └───────────┬─────────────┘
#                        YES    │     NO
#                         │     │
#                         ▼     ▼
#                  ┌───────┐  ┌──────────────────┐
#                  │  ""   │  │ Build half counts│
#                  └───────┘  └────────┬─────────┘
#                                       │
#                                       ▼
#                               ┌───────────────┐
#                               │ prefix = ""   │
#                               └───────┬───────┘
#                                       │
#                                       ▼
#                          ┌────────────────────────┐
#                          │ For each position i    │
#                          │ in first half          │
#                          └───────────┬────────────┘
#                                      │
#                                      ▼
#                          ┌────────────────────────┐
#                          │ Try chars 'a' → 'z'    │
#                          └───────────┬────────────┘
#                                      │
#                                      ▼
#                          ┌────────────────────────┐
#                          │ Temporarily choose     │
#                          │ character j            │
#                          └───────────┬────────────┘
#                                      │
#                                      ▼
#                   ┌──────────────────────────────────┐
#                   │ Build LARGEST possible remaining │
#                   │ characters (descending order)    │
#                   └───────────────┬──────────────────┘
#                                   │
#                                   ▼
#                        ┌─────────────────────────┐
#                        │ Build maximum possible │
#                        │ palindrome              │
#                        └───────────┬─────────────┘
#                                    │
#                                    ▼
#                          ┌────────────────────┐
#                          │ candidate > target?│
#                          └─────────┬──────────┘
#                               NO   │    YES
#                                │   │
#                                ▼   ▼
#                          ┌────────┐ ┌────────────────┐
#                          │ Undo   │ │ Lock character │
#                          │ choice │ │ in prefix      │
#                          └───┬────┘ └───────┬────────┘
#                              │              │
#                              │              ▼
#                              │       ┌──────────────┐
#                              │       │ Next position│
#                              │       └──────┬───────┘
#                              │              │
#                              └──────────────┘
#                                             │
#                                             ▼
#                                   ┌──────────────────┐
#                                   │ All half chars   │
#                                   │ constructed?     │
#                                   └────────┬─────────┘
#                                            │
#                                            ▼
#                                   ┌──────────────────┐
#                                   │ Mirror prefix    │
#                                   │ + middle if odd  │
#                                   └────────┬─────────┘
#                                            │
#                                            ▼
#                                     ┌────────────┐
#                                     │   Return   │
#                                     └────────────┘
# ```

# ---

# # 6. The algorithm in one picture

# The easiest way to remember it is:

# ```text
#              s
#              │
#              ▼
#        Count frequencies
#              │
#              ▼
#      Can s form palindrome?
#           /       \
#         NO         YES
#         │           │
#         ""          ▼
#              Take half counts
#                     │
#                     ▼
#              Build prefix
#              left → right
#                     │
#                     ▼
#           Try 'a' → 'z'
#                     │
#                     ▼
#         ┌────────────────────┐
#         │ "Can this choice   │
#         │ lead to > target?" │
#         └─────────┬──────────┘
#                   │
#                   ▼
#        Build LARGEST completion
#                   │
#                   ▼
#           largest palindrome
#                   │
#           ┌───────┴───────┐
#           │               │
#         <= target       > target
#           │               │
#           ▼               ▼
#         reject          accept
#           │               │
#           │               ▼
#           │        continue prefix
#           │               │
#           └───────────────┘
#                           │
#                           ▼
#                        mirror
#                           │
#                           ▼
#                        answer
# ```

# ---

# # 7. Complexity

# For your **exact implementation**:

# Let `H = n / 2`.

# For every position:

# ```python
# for j in range(26):
# ```

# we may construct the remaining string, which can take `O(n)`.

# So:

# ```text
# O(H × 26 × n)
# ```

# Since `H = n/2` and 26 is constant:

# ```text
# O(n²)
# ```

# Space:

# ```text
# O(n)
# ```

# for the constructed strings.

# ### Interview answer:

# > **Time: O(26n²), effectively O(n²) because the alphabet is fixed at 26. Space: O(n).**

# ---

# ## The one sentence I want you to remember

# If the interviewer asks **"What's the greedy idea?"**, say:

# > **At each position, I choose the smallest available character whose largest possible completion can still produce a palindrome strictly greater than the target.**

# That's the essence of your solution.
