def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(a,b,n):
    count = 0
    while a<=n and b<=n:
        if a<=b:
            a+=b
        else:
            b+=a
        count +=1
    print(count)
    

t = int(input())
while t!=0:2
1 2 3
5 4 100

    t-=1
    arr = inlt()
    run(arr[0],arr[1],arr[2])