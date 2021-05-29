def pref_func(a):
    l = len(a)
    Count = [0] * l  
    Count[0] = 0
    for i in range (l - 1):
        j = Cout[i]
        while (j > 0) and (a[i + 1] != a[j]):
            j = Count[j - 1]
        if (a[i + 1] == a[j]):
            Count[i+1] = j + 1
        else:
            Count[i + 1] = 0
    return Count

t = str(input())
a = list(t)

l = len(a)
pref = pref_func(a)

for i in range(l - 1, l):
    result = l - pref[i]

if (l % result == 0):
    print(l // result)
else:
    print('1')