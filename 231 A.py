count = 0
n = int(input())
for i in range(n):
    intQ = []
    q = input()
    q = q.split(' ')
    for j in q:
        intQ.append(int(j))
    if sum(intQ)>=2:
        count += 1
print(count)