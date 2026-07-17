def previous_greater_unique(arr):
    stack = []
    hash_map = {}

    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()

        if stack:
            hash_map[num] = stack[-1]
        else:
            hash_map[num] = -1

        stack.append(num)

    return hash_map

def previous_greater(arr):
    stack = []
    result = []

    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(num)

    return result