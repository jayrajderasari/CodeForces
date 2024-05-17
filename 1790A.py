def run(inp):
    pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

    count = 0
    for i in range(len(inp)):
        if pi[i] == inp[i]:
            count+=1
        else:
            break
    print(count)
    return
t = int(input())
while t!=0:
    t-=1
    i = input()
    run(i)