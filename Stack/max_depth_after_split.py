# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

# * We track the current **parentheses depth** while traversing the string.
# * For every `(`, we increment depth and assign it to group `depth % 2`; for `)`, we assign the current group before decrementing.
# * This alternates nested parentheses between the two groups, keeping each group's maximum depth balanced.
# * **Time:** `O(n)` | **Space:** `O(n)` for the result array.


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)
        depth = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                depth += 1
                ans[i] = depth % 2
            else:
                ans[i] = depth % 2
                depth -= 1
        return ans