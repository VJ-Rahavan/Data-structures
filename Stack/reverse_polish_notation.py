class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # truncate toward 0
            else:
                stack.append(int(token))

        return stack[-1]

# Traverse the tokens once while maintaining a stack.
# Push operands onto the stack.
# When an operator appears, pop the top two operands, evaluate the expression, and push the result back.
# At the end, the stack contains only one value, which is the final answer.

# Time: O(n)
# Space: O(n)