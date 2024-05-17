def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

n = int(input())
laptops = []
for i in range(n):
    input1 = inlt()
    laptops.append(input1)

invalid = []
cost = []
for i in laptops:
    for j in laptops:
        if i[0]<j[0] and i[1]<j[1] and i[2]<j[2]:
            invalid.append(i)
for i in range(len(laptops)):
    if laptops[i] not in invalid:
        cost.append(([laptops[i][-1]],i+1))
cost.sort()
print(cost[0][1])