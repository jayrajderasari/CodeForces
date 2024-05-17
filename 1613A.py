def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(a,b):
    if len(a[0]) + int(a[1]) > len(b[0]) + int(b[1]):
        print('>')
        return
    elif len(a[0]) + int(a[1]) < len(b[0]) + int(b[1]):
        print('<')
        return
    else:
        if int(a[1])>int(b[1]):
            for i in range(int(a[1])-int(b[1])):
                a[0] += '0'
        else:
            for i in range(int(b[1])-int(a[1])):
                b[0] += '0'
        if int(a[0])>int(b[0]):
            print('>')
        elif a[0] == b[0]:
            print('=')
        else:
            print('<')
        
t =int(input())
while t!=0:
    t-=1
    a = input()
    a = a.split(' ')
    b = input()
    b = b.split(' ')
    run(a,b)