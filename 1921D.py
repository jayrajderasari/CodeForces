def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,m,inp1,inp2):
    result = []
    inp1.sort()
    inp2.sort()
    c = 0
    while len(inp1)!=0:
        if c == 0:
            result.append(abs(inp1[0]-inp2[-1]))
            inp1.pop(0)
            inp2.pop(-1)
            c = 1
        else:
            result.append(abs(inp1[-1]-inp2[0]))
            inp2.pop(0)
            inp1.pop(-1)
            c = 0                    
    sumation = sum(result)
    print(sumation)

t = int(input())
while t!=0:
    t-=1
    inp = inlt()
    n,m = inp[0],inp[1]
    inp1 = inlt()
    inp2 = inlt()
    run(n,m,inp1,inp2)