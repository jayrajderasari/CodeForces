def inp():
    return(int(input()))
# 1
# 1

def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def insr():
    s = input()
    return(list(s[:len(s) - 1]))
# 1 2 3
# ['1', ' ', '2', ' ']

def invr():
    return(map(int,input().split()))
# 1 2 3
# <map object at 0x000001C7CFFDA9E0>

i = inp()
print(i)
i = inlt()
print(i)
i = insr()
print(i)
i = invr()
print(i)
