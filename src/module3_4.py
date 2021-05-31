def pref_func(s):
    length = len(s)
    Meter = [0] * length    
    Meter[0] = 0
    for i in range (length - 1):
        j = Meter[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = Meter[j - 1]
        if (s[i + 1] == s[j]):
            Meter[i+1] = j + 1
        else:
            Meter[i + 1] = 0
    return Meter
text = str(input())
s = list(text)

length = len(s)
pref = pref_func(s)
print(length - pref[-1]) 