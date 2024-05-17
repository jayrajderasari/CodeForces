
def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(n,m,inp):
    passanger = 0
    bus = 1
    for i in inp:
        passanger += i
        if passanger>m:
            bus +=1
            passanger = i
    print(bus)



inp = inlt()
n,m = inp[0],inp[1]
inp = inlt()
run(n,m,inp)