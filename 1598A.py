def run(n,a,b):
    for i in range(n):
        if a[i] == b[i] == '1':
            print('NO')
            return
    print('YES')
    return

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = input()
    b = input()
    run(n,a,b)