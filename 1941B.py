def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
def run(inp,n):
    i = 1
    while i<n-1:
        if inp[i-1] < 0:
            break
        if inp[i-1] !=0:
            inp[i] -= inp[i-1]*2
            inp[i+1] -= inp[i-1]
            inp[i-1] = 0
        i+=1
        # print(inp)
    for i in inp:
        if i !=0:
            print('NO')
            return
    print('YES')


t = int(input())
while t!=0:
    t-=1
    n = int(input())
    c = inlt()
    run(c,n)