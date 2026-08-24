# Boyer-Moore Voting Algorithm.
# I maintain a candidate and a count. When count hits 0, I pick the current element
# as the new candidate. If the current element matches the candidate, I increment count,
# otherwise I decrement it. The majority element (appears > n/2 times) always survives
# because its count can never be cancelled out completely.
# Time: O(n), Space: O(1).

def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
