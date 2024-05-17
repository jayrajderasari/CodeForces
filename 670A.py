n = int(input())
a = n//7
b = n%7
miniHoli = 2*a
maxiholi = 2*a
if b==6:
    miniHoli += 1

if b>=2:
    maxiholi = 2*a+2
elif b == 1:
    maxiholi = 2*a+1
print(miniHoli,maxiholi)