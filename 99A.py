def run(inp):
    ans = 0
    s = str(inp)
    intS = ''

    for i in range(len(s)):
        if s[i] == '.':
            frac = int(s[i+1])
            break
        else:
            intS += s[i]
    if intS[-1] == '9':
        print('GOTO Vasilisa.')
    else:    
        if frac<5:
            ans = int(intS)
        else:
            ans = int(intS)+1
        print(ans)
    return
inp = input()
run(inp)