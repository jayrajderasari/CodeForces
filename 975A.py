n = int(input())
arr = input()
arr = arr.split(' ')
s1 = set()
for i in arr:
    s = []
    for j in i:
        if j not in s:
            s.append(j)
    s.sort()
    s = ''.join(s)
    s1.add(s)
print(len(s1))