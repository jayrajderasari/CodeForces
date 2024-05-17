def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(i,n):
    if n[i-1]!=0 and n[(n[i-1]-1)]!=0:
        print('YES')
    else:
        print('NO')

t = int(input())
while t!=0:
    t-=1
    i = int(input())
    n = inlt()
    run(i,n)