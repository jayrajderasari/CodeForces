def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(l,n):
    sum = 0
    for i in l:
        sum = sum + abs(i)
    print(sum)
    return 

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    l = inlt()
    run(l,n)