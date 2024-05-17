t = int(input())

while t!=0:
    data = []
    str = input()
    str = str.split()
    m = int(str[0])
    n = int(str[1])
    for i in range(0,m):
        data.append(input())
    name = ""

    for col in range(0,n):
        if name == "":
            for row in range (0,m):
                if data[row][col] == "v":
                    name = name + 'v'
                    break
            
        elif name == "v":
            for row in range (0,m):
                if data[row][col] == "i":
                    name = name + 'i'
                    break
        elif name == "vi":
            for row in range (0,m):
                if data[row][col] == "k":
                    name = name + "k"
                    break
        elif name == "vik":
            for row in range (0,m):
                if data[row][col] == "a":
                    name = name + "a"
                    break
        if name == "vika":
            break
    if(name == "vika"):
        print("YES")
    else:
        print("NO")
    t = t-1