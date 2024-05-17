def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,arr):
    arr.sort()
    ans = abs(arr[n]-arr[n-1])
    print(ans)
t = int(input())
while t!=0:
    t-=1
    n = int(input())
    arr = inlt()
    run(n,arr)