def inlt():
    return(list(map(int,input().split())))
# 1 2 3
# [1, 2, 3]

def run(input1):
    for i in range(3):
        for j in range(3):
            whiteCount = 0
            blackCount = 0
            if input1[i][j] == '.':
                whiteCount+= 1
            else:
                blackCount += 1
            if input1[i+1][j] == '.':
                whiteCount+= 1
            else:
                blackCount += 1
            if input1[i][j+1] == '.':
                whiteCount+= 1
            else:
                blackCount += 1
            if input1[i+1][j+1] == '.':
                whiteCount+= 1
            else:
                blackCount += 1

            out = max(whiteCount,blackCount)
            if out >=3:
                    print("YES")
                    return
    print("NO")
    return

input1 = []
for _ in range(4):
    temp = str(input())
    input1.append(temp)
run(input1)