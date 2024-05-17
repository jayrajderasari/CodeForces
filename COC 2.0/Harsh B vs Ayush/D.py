def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
from collections import Counter

n = int(input())
arr = inlt()

freq = Counter(arr)
x = 0
for f in freq:
    x += freq[f]//2
print(x//2)