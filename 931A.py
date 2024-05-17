def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,arr):
    arr.sort()
    # print(arr)
    i = arr[0]    
    j = arr[-1]
    k = arr[1]    
    l = arr[-2]    
    s = abs(i-j) + abs(j-k) + abs(k-l) + abs(i-l)
    print(s)

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = inlt()
    run(n,a)