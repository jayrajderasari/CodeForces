def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

s = inlt()
n , m = s[0],s[1]
l = []
best = [0]*m
for i in range(n):
    std = [int(i) for i in input()]
    l.append(std)
    for j in range(m):
        best[j] = max(best[j],std[j])
count = 0
for i in l:
    for j in range(m):
        if i[j] == best[j]:
            count += 1
            break
print(count)