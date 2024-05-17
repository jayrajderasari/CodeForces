def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(arr):
    a = 0
    i = 0
    while i<len(arr)-2:
        a = arr[i]
        if arr[i+1]>arr[i]:
            break 
        i += 1
    j = i+1

    while j<len(arr)-1:
        b = arr[j]
        if arr[i]<arr[j+1]:
            break
        else:
            i += 1
        j += 1

    k = j+1
    while k<len(arr):
        c = arr[k]
        if arr[j]>arr[i]:
            break
        else:
            j += 1
        k += 1 
    if k<len(arr):
        print('YES')
        print(i,j,k)
    else: 
        print('NO')


t = int(input())
for _ in range(t):
    n = int(input())
    arr = inlt()
    run(arr)