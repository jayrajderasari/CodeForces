def run(n,s,f):
    count1 = 0
    count2 = 0
    for i in range(n):
        if s[i] != f[i]:
            if s[i] == '1':
                count1 += 1
            else:
                count2 += 1
    return max(count1,count2)    

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    s = input()
    f = input()
    print(run(n,s,f))