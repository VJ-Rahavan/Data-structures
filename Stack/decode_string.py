# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

#My approach is to use a stack to keep track of the characters and numbers.
# When I encounter a closing bracket, I pop characters from the stack until I find the corresponding opening bracket. 
# I then pop the number from the stack, which tells me how many times to repeat
# the substring. I push the repeated substring back onto the stack.


def decode_str(s: str) -> str:
    stack = []
    
    for i in s:
        if i == "]":
            temp = ""
            while stack and stack[-1] != "[":
                temp = stack.pop() + temp
            stack.pop()
            
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
        
            stack.append(int(num) * temp)
        else:
            stack.append(i)
    
    print("".join(stack))

decode_str("3[a]2[bc]")


# Alternate Approach

# I use two stacks: one for numbers and one for strings.
# I traverse the string character by character.
# When I encounter a digit, I build the current number.
# When I encounter an opening bracket, I push the current number onto the number stack and reset the current number.
# When I encounter a closing bracket, I pop the top number from the number stack and the top string from the string stack, and I repeat the string accordingly.
# When I encounter a letter, I append it to the current string.
# At the end, I join all the strings in the string stack to form the final decoded string.

class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return s
        
        currNum = 0
        intStack = []
        strStack = []

        for x in s:
            if x.isdigit():
                currNum = (currNum * 10) + int(x)
            else:
                if x == '[':
                    intStack.append(currNum)
                    currNum = 0
                    strStack.append(x)
                elif x == ']':
                    temp = ""
                    while strStack and strStack[-1] != "[":
                        temp = strStack.pop() + temp
                    strStack.pop() # Remove "["
                    
                    num = intStack.pop()
                    # Multiply and push back
                    strStack.append(temp * num)
                else:
                    strStack.append(x)
                    
        ans = ""
        while strStack:
            ans = strStack.pop() + ans
            
        return ans
