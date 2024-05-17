def run(inp):
    count4 = 0
    count7 = 0
    for i in inp:
        if i == '4':
            count4 += 1
        elif i == '7':
            count7 += 1

    if count4 == count7 == 0:
        return -1
    elif count4 == max(count4,count7):
        return 4
    else:
        return 7 
    
inp = str(input())
print(run(inp))
