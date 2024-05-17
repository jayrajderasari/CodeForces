def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
def run(inp,n):
    count = 0
    i = 0
    while i<n-2:
        if inp[i]=='m' and inp[i+1]=='a' and inp[i+2]=='p':
            count+=1
            i += 3
        elif inp[i]=='p' and inp[i+1]=='i' and inp[i+2]=='e':
            count+=1
            i += 3
        else:
            i+=1

    print(count)



t = int(input())
while t!=0:
    t-=1
    n = int(input())
    c = input()
    run(c,n)