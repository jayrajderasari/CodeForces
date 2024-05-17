def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]


n = int(input())
sumMap = {}
diffMap = {}
count = 0
for _ in range(n):
    temp = inlt()
    x = temp[0]
    y = temp[1]
    if x+y in sumMap:
        count += sumMap[x+y]
        sumMap[x+y] += 1
    else:
        sumMap[x+y] = 1
    if (x-y) in diffMap:
        count += diffMap[(x-y)]
        diffMap[(x-y)] += 1
    else:
        diffMap[(x-y)] = 1

print(count)