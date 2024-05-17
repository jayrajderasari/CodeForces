def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,f,a,b,inp):
    count = 0
    inp.insert(0,0)
    for i in range(n):
        diff = (inp[i+1]-inp[i])*a
        count += min(diff,b)
    if count<f:
        print('YES')
    else:
        print('NO')


t = int(input())
while t!=0:
    t-=1
    inp = inlt()
    n,f,a,b = inp[0],inp[1],inp[2],inp[3]
    inp = inlt()
    run(n,f,a,b,inp)
