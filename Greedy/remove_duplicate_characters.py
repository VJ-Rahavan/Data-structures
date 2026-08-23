# I use a greedy + stack approach. 
# I keep character frequencies to know whether a character can be safely removed.

# For each character, if it’s already in the stack, I skip it. 
# Otherwise, while the stack top is larger than the current character and appears again later, I pop it. 
# Then I push the current character.

# This ensures every character appears once and gives the lexicographically smallest result.

# Time: O(n), Space: O(k).

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = {}

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        stack = []

        for ch in s:
            seen[ch] -= 1

            if ch in stack:
                continue

            while stack and stack[-1] > ch and seen[stack[-1]] > 0:
                stack.pop()

            stack.append(ch)

        return "".join(stack)