def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(a,b,c,d):
    ab = (((a[0]-b[0])**2)+((a[1]-b[1])**2))**(1/2)
    ac = (((a[0]-c[0])**2)+((a[1]-c[1])**2))**(1/2)
    l = int(min(ab,ac))
    print(l*l)
    return 

t = int(input())
while (t!=0):
    t-=1
    a = inlt()
    b = inlt()
    c = inlt()
    d = inlt()
    run(a,b,c,d)