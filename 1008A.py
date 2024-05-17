word = input()
validConsonant = 0
word = word.lower()
vovels = ['a','e','i','o','u']
for w in word:
    if validConsonant>1:
        break
    elif w in vovels or (w == 'n' and validConsonant == 0):
        validConsonant = 0
    else:
        validConsonant += 1
if validConsonant>=1:
    print('NO')
else:
    print('YES')