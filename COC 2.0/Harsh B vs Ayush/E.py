def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

inp = inlt()
n,m=inp[0],inp[1]
inp = []
for _ in range(n):
    i = inlt()
    inp.append(i)
l = inp
flag = 0
for i in range(n):
    if l[i][0]==1 or l[i][-1] ==1:
        flag = 1
        break
for i in range(m):
    if l[0][i] == 1 or l[-1][i]==1:
        flag = 1
        break
if flag == 1:
    print(2)
else:
    print(4)