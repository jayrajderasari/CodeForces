def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

n = int(input())
inp = inlt()
s = set()
j = len(inp)-1
ans = []

while j>=0:
    if inp[j] not in s:
        ans.append(inp[j])
        s.add(inp[j])
    j-=1
ans.reverse()
print(len(ans))
for i in ans:
    print(i)

