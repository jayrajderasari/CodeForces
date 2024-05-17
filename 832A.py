def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

inp1 = inlt()
n = inp1[0]
k = inp1[1]
totalMoves = n//k

if totalMoves%2 == 1:
    print("YES")
else:
    print("NO")