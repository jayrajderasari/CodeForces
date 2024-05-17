def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

inp = inlt()
n,k = int(inp[0]), int(inp[1])
inp = inlt()
inp.sort()
inp = list(set(inp))

count = 0
arr = []
for i in range(n):
    if sum(arr) > k:
        break
    else:
        arr.append(inp[i])
        count+=1
print(count)
print(arr)