def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

n = int(input())
input1 = inlt()
input1.sort()
total = sum(input1)
if total%2 == 0:
    print(total)
else:
    for i in input1:
        if i%2==1:
            print(total-i)
            break