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