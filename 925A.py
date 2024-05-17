def run(n):
    if n<=28:
        a = chr(96+1)
        b = chr(96+1)
        c = chr(96+n-2)
    elif 28<n<=53:
        a = chr(96+1)
        b = chr(96+n-27)
        c = chr(96+26)
    else:
        a = chr(96+n-52)
        b = chr(96+26)
        c = chr(96+26)
    s = a+b+c
    print(s)

t = int(input())
while t>0:
    n = int(input())
    run(n)
    t-=1