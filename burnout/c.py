def recc(nums):
    if nums == []:
        result = [[]]
        return result
    result = recc(nums[1:])
    return (result + [[nums[0]] + y for y in result]) 

n = int(input())
s = int(input()) # flower limit
flowers = (input())
flowers = flowers.split()
print(flowers)
subsets = recc(flowers)
result = []
for i in subsets:
    sum = 0
    for j in i:
        sum = sum + int(j) 
    result.append(sum)

print(result)
result.pop(0)
sorted = result
result.sort()
print(result)
i = 0
while i < len(result):
    if result[i]>s:
        i = i - 1
        break
    i = i+1
for j in range(0,len(result)):
    if result[j] == i:
        print(len(subsets[j]))
        break