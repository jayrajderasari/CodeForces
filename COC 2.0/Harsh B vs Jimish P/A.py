def run(inp):
    count = 0
    i = 0
    while i <len(inp):
        if inp[i] == '1':
            break
        i += 1
    j = len(inp)-1
    while j >=0:
        if inp[j] == '1':
            break
        j -= 1
    inp = inp[i:j]
    for s in inp:
        if s == '0':
            count += 1
    print(count)
        


t = int(input())
while t!= 0:
    t-=1
    inp = input()
    run(inp)
