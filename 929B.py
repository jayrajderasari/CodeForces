def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(l,n):
    s = sum(l)
    if s%3 == 0:
        print(0)
        return
    elif s%3 == 2:
        print(1)
        return
    else:
        for i in l:
            if i%3==1:
                print(1)
                return
        print(2)
        return


t = int(input())
while t!=0:
    t-=1
    n = int(input())
    l = inlt()
    run(l,n)