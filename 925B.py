def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,inp):
    target = sum(inp)/n
    balance = 0
    for i in range(n):
        if balance<0:
            print('NO')
            return
        if inp[i] == target:
            continue
        elif inp[i]>target:
            balance += inp[i]-target
            inp[i] = target
        else:
            balance -= target - inp[i]
            inp[i] = target
    print('YES')
t = int(input())
while t>0:
    n = int(input())
    inp = inlt()
    run(n,inp)
    t-=1