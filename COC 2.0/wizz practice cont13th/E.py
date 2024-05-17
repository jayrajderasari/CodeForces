def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

inp = inlt()
n = inp[0]
k = inp[1]
atSale = inlt()
aftrSale = inlt()

spend = 0
d = dict()
diffArr = []
for i in range(n):
    diffArr.append(atSale[i]-aftrSale[i])
sumation = sum(atSale)
diffArr.sort(reverse=True)
index = 0
z = n-k
while(z>0):
    z-=1
    if diffArr[index]>=0:
        sumation = sumation-diffArr[index]
        index+=1
print(sumation)