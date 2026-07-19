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

#Test cases to validate the implementation of previous_greater_unique and previous_greater
if __name__ == "__main__":
    arr1 = [4, 5, 2, 10, 8]
    expected_output1 = {4: -1, 5: 4, 2: 5, 10: 5, 8: 10}
    assert previous_greater_unique(arr1) == expected_output1, "Test Case 1 Failed"

    arr2 = [4, 5, 2, 10, 8]
    expected_output2 = [-1, 4, 5, -1, 10]
    assert previous_greater(arr2) == expected_output2, "Test Case 2 Failed"

    arr3 = [3, 7, 1, 7]
    expected_output3 = {3: -1, 7: -1, 1: 7}
    assert previous_greater_unique(arr3) == expected_output3, "Test Case 3 Failed"

    arr4 = [3, 7, 1, 7]
    expected_output4 = [-1, -1, 7, -1]
    assert previous_greater(arr4) == expected_output4, "Test Case 4 Failed"

    print("All test cases passed!")