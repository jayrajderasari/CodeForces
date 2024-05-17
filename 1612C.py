def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

# def run(k,x):
    # sumation = 0
    # count = 0
    # if k == 1:
    #     if x>1:
    #         print(1)
    #         return
    # for i in range(1,k+1):
    #     if sumation<x:
    #         sumation += i
    #         count +=1
    #     else:
    #         print(count)
    #         return
            
    # for i in range(k,0,-1):
    #     if sumation<x:
    #         sumation += i*(i+1)/2
    #         count +=1
    #     else:
    #         print(count)
    #         return
    # print(count)
def sumation(k):
        return k*(k+1)//2
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

def run(k,x):
    i = 1
    j = 2*k-1
    res = 2*k-1
    over = False
    while i<=j:
        mid = (i+j)//2
        if (mid>=k):
            over = (sumation(k)+sumation(k-1)-sumation(2*k -1 -mid)>=x)
        else:
            over = (sumation(mid)>=x)
        if over:
            res = mid
            j = mid-1
        else:
            i = mid+1

    return res
t = int(input())
for _ in range(t):
    arr = inlt()
    k = int(arr[0])
    x = int(arr[1])
    print(run(k,x))