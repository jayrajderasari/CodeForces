def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,arr):
    i = 0
    print(3*n)
    while i<n-1:
        if arr[i]<arr[i+1]:
            print('2',i+1,i+2)
            print('1',i+1,i+2)
            print('2',i+1,i+2)
            print('1',i+1,i+2)
            print('2',i+1,i+2)
            print('1',i+1,i+2)
        else:
            print('1',i+1,i+2)
            print('2',i+1,i+2)
            print('1',i+1,i+2)
            print('2',i+1,i+2)
            print('1',i+1,i+2)
            print('2',i+1,i+2)
        i += 2
        

t = int(input())
arr = []
while t!=0:
    t-=1
    n = int(input())
    arr = inlt()
    run(n,arr)