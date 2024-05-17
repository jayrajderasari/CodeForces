n = int(input())
s = int(input()) # flower limit
flowers = (input())
flowers = flowers.split()
flowers.sort()
sum = 0
result = 0
for i in range(0,n):
    if (sum + int(flowers[i]))<=s:
        sum = sum + int(flowers[i])
        result = result+1
    else:
        break
print(result)