def run(s):
    i = 0
    j = len(s)-1
    while s[i] == 'W':
        i +=1
    while s[j] == 'W':
        j -= 1
    print(j-i+1)

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    s = str(input())
    run(s)