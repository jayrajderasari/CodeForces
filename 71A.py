def run(s):
    if len(s)>10:
        s = s[0]+str(len(s)-2)+s[-1]
    print(s)

t = int(input())
while t!=0:
    s = input()
    run(s)
    t-=1