def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def positionCalculator(a,b,x):
    arr = set()
    arr.add((x[0]+a,x[1]+b))
    arr.add((x[0]+b,x[1]+a))
    
    arr.add((a+x[0],x[1]-b))
    arr.add((b+x[0],x[1]-a))

    arr.add((x[0]-a,b+x[1]))
    arr.add((x[0]-b,a+x[1]))
    
    arr.add((x[0]-a,x[1]-b))
    arr.add((x[0]-b,x[1]-a))
    return arr

def run(a,b,king,queen):
    kingPosition = positionCalculator(a,b,king)
    queenPosition = positionCalculator(a,b,queen)
    count = 0
    for i in kingPosition:
        if i in queenPosition:
            count+=1
    print(count)
    return

t = int(input())
while t!= 0:
    t-=1
    a = inlt()
    a,b = a[0],a[1]
    king = inlt()
    queen = inlt()
    run(a,b,king,queen)