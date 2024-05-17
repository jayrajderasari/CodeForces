def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]
def insr():
    s = input()
    return(list(s[:len(s)]))
# 1 2 3
# ['1', ' ', '2', ' ']

def run(inp):
    prev = -1
    for i in inp:
        temp = i[0]
        for j in i:
            if j != temp or temp == prev:
                print('NO')
                return
        prev = temp
    print('YES')
    return

a = inlt()
n = a[0]
m = a[1]
inp = []
for i in range(n):
    inp1 = insr()
    inp.append(inp1)
run(inp)