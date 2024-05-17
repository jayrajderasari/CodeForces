from math import gcd
p = int(input())
x = 2
count = 1
while x<p:
	if (x**(p-1)-1)/(p) == (x**(p-1)-1)//(p):
		count+=1
	x+=1
print(count)