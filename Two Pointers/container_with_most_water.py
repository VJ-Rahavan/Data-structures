# "I use two pointers at the start and end. 
# At each step, the area is bounded by the shorter wall,
#  so I move the pointer at the shorter side inward — 
# since moving the taller one can never increase area, 
# only shrink width for the same or lower height cap. 
# I track the max area seen until the pointers meet. 
# This runs in O(n) time and O(1) space."

def find_most_water(arr):
    start = 0
    end = len(arr) - 1
    most_water = 0
    
    while start < end:
        temp = (end - start) * min(arr[start],arr[end])
        
        most_water = max(temp,most_water)
            
        if arr[start] < arr[end]:
            start+=1
        else:
            end-=1
    print(most_water)
    

find_most_water([1,8,6,2,5,4,8,3,7])
