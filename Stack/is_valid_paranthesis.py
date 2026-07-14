# I use a stack to store opening brackets. 
# I keep a hash map that maps each closing bracket to its corresponding opening bracket. 
# When I encounter an opening bracket, I push it onto the stack. 
# When I encounter a closing bracket, I first ensure the stack isn't empty, 
# then pop the top element and compare it with the expected opening bracket from the hash map. 
# If they don't match, the string is invalid. At the end, the stack must be empty, 
# otherwise there are unmatched opening brackets.

def is_valid_paran(s):
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch not in pairs:      # Opening bracket
            stack.append(ch)
        else:                    # Closing bracket
            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return not stack


print(is_valid_paran("({)}[]{}"))