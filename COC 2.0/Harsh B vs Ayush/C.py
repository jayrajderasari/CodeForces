def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
 
inp = inlt()
 
c,u,v,a,l = inp[0],inp[1],inp[2],inp[3],inp[4]
 
 
read = u
i = 1
days = 1
while read<=c:
    if u+(i*a) < v:
        read = read + (u+(i*a)) - l
    else:
        read = read + v - l
    i += 1
    days+=1
print(days)