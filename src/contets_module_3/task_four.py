def pref_func(s):
    l = len(s)
    Count = [0] * l 
    Count[0] = 0
    for i in range (l - 1):
        j = Count[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = Count[j - 1]
        if (s[i + 1] == s[j]):
            Count[i+1] = j + 1
        else:
            Count[i + 1] = 0
    return Count
text = str(input())
s = list(text)

l = len(s)
pref = pref_func(s)
print(l - pref[-1])