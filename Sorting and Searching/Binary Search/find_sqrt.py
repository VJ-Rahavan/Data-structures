# But mathematically, √-4 is not a real number.
# (2i is a square root in the complex-number system.)

def find_sqrt(num):
    if num < 0:
        return -1
    
    start = 0 
    end = num
    ans = 0
    
    while start <= end:
        mid = (start+end) // 2
        mid_prod = mid * mid
        if mid_prod == num:
            return mid
        elif mid_prod < num:
            ans = mid
            start = mid + 1
        else:
            end = mid -1
    
    return ans

print(find_sqrt(25))