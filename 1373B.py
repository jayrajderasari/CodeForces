def run(s):
    count0 = 0
    count1 = 0
    for i in s:
        if i == '0':
            count0 += 1
        else:
            count1 += 1
    pairs = min(count1,count0)
    if pairs%2 == 1:
        print('DA')
    else:
        print('NET')

t = int(input())
for _ in range(t):
    s = input()
    out = run(s)

