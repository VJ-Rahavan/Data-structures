class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        res = ""

        for i in s:
            if i == ")":
                temp = ""
                while stack and stack[-1] != "(":
                    temp = temp + "".join(reversed(stack.pop()))
                stack.pop()
                stack.append(temp)
            else:
                stack.append(i)
        return "".join(stack)