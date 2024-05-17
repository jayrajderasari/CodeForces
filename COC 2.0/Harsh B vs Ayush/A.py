def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

n = int(input())
arr = inlt()
ans = 0
for i in arr:
    if i<0:
        ans -= i
    else:
        ans += i
print(ans)