def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(x,y):
    steps = 0
    while x!= 0 and y!=0:
        steps += 2
        x-=1
        y-=1
    if x!= 0:
        steps += (2*x)-1
    elif y != 0:
        steps += (2*y)-1
    print(steps)
    return


t = int(input())
while t!=0:
    t-=1
    inp = inlt()
    run(inp[0],inp[1])
