import math
def count_distinct_k(a, b, l):
    ans = 0
    arr = []
    i = 1
    j = 1
    while i<=l:
        j = 1
        while j<=l:
            temp = i*j
            if l%temp == 0 and temp not in arr:
                arr.append(temp)
                ans+=1
            j=j*b
        i = i*a
    return ans

t = int(input())
for _ in range(t):
    a, b, l = map(int, input().split())
    result = count_distinct_k(a, b, l)
    print(result)
