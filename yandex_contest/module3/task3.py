def prefix(s):
    dlina = len(s)
    k = [0] * dlina
    k[0] = 0
    for i in range(dlina - 1):
        j = k[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = k[j - 1]
        if (s[i + 1] == s[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k


inp = str(input())

dlina = len(inp)
pref = prefix(inp)

for i in range(dlina - 1, dlina):
    res = dlina - pref[i]

if (dlina % res == 0):
    print(dlina // res)
else:
    print(1)
