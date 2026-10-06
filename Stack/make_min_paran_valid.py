# 921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # unmatched '(' waiting for a ')'
        close_needed = 0  # unmatched ')' that need a '(' inserted

        for ch in s:
            if ch == "(":
                open_needed += 1
            elif open_needed:
                open_needed -= 1
            else:
                close_needed += 1

        return open_needed + close_needed