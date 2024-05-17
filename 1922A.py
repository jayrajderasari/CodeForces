def run(n,a,b,c):
    flag = False
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            flag = True
    if flag:
        print('YES')
        return
    else:
        print('NO')

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = input()
    b = input()
    c = input()
    run(n,a,b,c)