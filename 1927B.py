def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(arr):
    cnt = [0] * 26
    s = ''
    for i in range(n):
        for j in range(26):
            if cnt[j] == arr[i]:
                cnt[j] += 1
                s += chr(97 + j)
                break
    print(s)

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    s = inlt()
    run(s)