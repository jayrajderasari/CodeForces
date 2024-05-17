def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,inp):
    i = 0
    j = n-1
    temp = 0
    countA=1
    countB = 1
    while i<n-1 and inp[i] == inp[i+1]:
        i += 1
        countA += 1
    while j>0 and inp[j] == inp[j-1]:
        j -= 1
        countB += 1
    if i == n-1:
        cost = 0
        print(cost)
        return
    if inp[0] == inp[-1]:
        temp = countB+countA
    else:
        temp = max(countA,countB)
    cost = n-temp
    print(cost)


t = int(input())
while t>0:
    n = int(input())
    inp = inlt()
    run(n,inp)
    t-=1