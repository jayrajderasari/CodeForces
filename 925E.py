def determine_winner(n, x, arr):
    arr2 = []
    count1 = 0
    for s in arr:
        count = 0
        for c in reversed(s):
            if c == '0':
                count += 1
            else:
                break
        arr2.append(count)
        count1 += len(s) - count
    arr2.sort(reverse=True)
    for i in range(1, n, 2):
        count1 += arr2[i]
    if count1 > x:
        print("Sasha")
    else:
        print("Anna")




t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = (input())
    a = a.split(' ')
    determine_winner(n, m, a)
