t = int(input())
for _ in range(t):
    n = int(input())
    
    if(n<=9): 
        ans = (n)
    elif(n>=10 and n<=99):
        ans = 9
        ans += n//10
    elif(n>=100 and n<=999):
        ans = 18
        ans += n//100
    elif(n>=1000 and n<=9999):
        ans = 27
        ans += n//1000
    elif(n>=10000 and n<=99999):
        ans = 36
        ans += n//10000
    else:
        ans = 45
        ans += n//100000
    print(ans)