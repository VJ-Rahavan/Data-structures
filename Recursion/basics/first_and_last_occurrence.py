# Find first/last occurrence of an element in an array

def find(arr,ch,idx = 0, first = -1, last = -1):

  if len(arr) == idx:
    return [first,last]

  if arr[idx] == ch:
    if first == -1:
      first = idx
    last = idx

  return find(arr,ch,idx+1,first,last)



print(find([2,6,7,2,1,2,5],2))

#cleaner approach to find first and last occurrence of an element in an array using recursion
def firstOccurrence(arr, ch, idx=0):
    if idx == len(arr):
        return -1

    if arr[idx] == ch:
        return idx

    return firstOccurrence(arr, ch, idx + 1)


def lastOccurrence(arr, ch, idx=0):
    if idx == len(arr):
        return -1

    result = lastOccurrence(arr, ch, idx + 1)

    if result != -1:
        return result

    if arr[idx] == ch:
        return idx

    return -1