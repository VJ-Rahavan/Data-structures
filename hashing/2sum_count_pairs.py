# Input: arr[] = [1, 5, 7, -1, 5], target = 6
# 2 Sum - Count pairs with given sum

# I use a frequency map to store the numbers I have already seen.
# For each number, I calculate its complement as target - num 
# and check how many times that complement has appeared.
# I add that frequency to the answer, then store the current number in the map.
# This counts duplicates correctly and runs in O(n) time with O(n) space.

def find_sum(arr, target):
    freq = {}
    count = 0

    for num in arr:
        diff = target - num
        count += freq.get(diff, 0)
        freq[num] = freq.get(num, 0) + 1

    print(count)