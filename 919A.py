def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

inp1 = inlt()
n = inp1[0]
quantity = inp1[1]
cost = float('inf')
for i in range(n):
    inp2 = inlt()
    cost = min(cost,(inp2[0]/inp2[1])*quantity)
print(cost)