def three_sum(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        start = i + 1
        end = len(arr) - 1
        while start < end:
            tot = arr[i] + arr[start] + arr[end]
            if tot == 0:
                res.append([arr[i],arr[start],arr[end]])
                end-=1
                start+=1
                while start < end and arr[end] == arr[end + 1]:
                    end -= 1
                while start < end and arr[start] == arr[start - 1]:
                    start += 1
            elif tot > 0:
                end -= 1
            else:
                start += 1
    print(res)
    

three_sum([-1,0,1,1,2,-1,-4]);