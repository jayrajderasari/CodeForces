n = int(input())
i = 1
arr = []
while sum(arr)<=n:
    arr.append(i)
    i+=1
print(len(arr)-1)

diff = abs(n-sum(arr))

if diff in arr:
    arr.remove(diff)
for i in arr:
    print(i)