
def inlt():
    return (list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
def lcm(x,y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

input1 = input()
input1 = input1.split(' ')

x = int(input1[0])
y = int(input1[1])
a = int(input1[2])
b = int(input1[3])

bothColoured = lcm(x,y)
count = 0
i = a//bothColoured
j = b//bothColoured
if i==0:
    print(b//bothColoured)
else:
    if b%bothColoured == 0 or a%bothColoured == 0:
        print(j-i+1)
    else:
        print(j-i)