def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
dA = {}
aCompany = int(input())
for _ in range(aCompany):
    inp = inlt()
    drug = inp[0]
    profit = inp[1]
    dA[drug] = profit
bCompany = int(input())
for _ in range(bCompany):
    inp = inlt()
    drug = inp[0]
    profit = inp[1]
    if drug in dA:
        dA[drug] = max(dA[drug],profit)
    else:
        dA[drug] = profit
profit = 0
for i in dA:
    profit += dA[i]
print(profit)