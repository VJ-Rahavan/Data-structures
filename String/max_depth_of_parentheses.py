# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        maxx = 0
        curr = 0
        for i in s:
            if i == "(":
                curr += 1
                maxx = max(curr,maxx)
            elif i == ")":
                curr -= 1
            
        return maxx