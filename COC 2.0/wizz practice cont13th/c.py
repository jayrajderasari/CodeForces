def run(inp):
    count = 0
    count1 = 0
    for i in inp:
        if i == '1':
            count = 0
            count1 = 1
        elif i == '4' and count1 == 1:
                count += 1
        else:
            count += 5
        if count>2:
            print("NO")
            return
        
    print("YES")


inp = input()
run(inp)
