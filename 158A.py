def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def run(n,k,inp2):
    count = 0
    scoreK = inp2[k-1]
    for i in inp2:
        if i>=scoreK and i>0:
            count+=1
    print(count)

inp1 = inlt()
n = inp1[0]
k = inp1[1]
inp2 = inlt()
run(n,k,inp2)