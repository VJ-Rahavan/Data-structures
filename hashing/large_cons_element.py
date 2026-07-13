# I store all numbers in a set so I can check existence in O(1). 
# Then I iterate through each number and only start counting 
# if it's the beginning of a sequence, which I detect by checking that num - 1 is not in the set.
#  From there, I keep extending the sequence while num + 1 exists and update the maximum length. 
# Since each sequence is traversed only once, the overall time complexity is O(n)."

def long_cons_elements(arr):
    res = 0
    freq = set(arr)
    for i in arr:
        if i - 1 not in freq:
            cur = i
            length = 1
            while cur + 1 in freq:
                cur += 1
                length += 1
            
            res = max(res, length)

    print(res)

long_cons_elements([100,4,200,1,3,2,8,9])