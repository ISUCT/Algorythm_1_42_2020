def pref_func(s):
    length = len(s)
    Counter = [0] * length    
    Counter[0] = 0
    for i in range (length - 1):
        j = Counter[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = Counter[j - 1]
        if (s[i + 1] == s[j]):
            Counter[i+1] = j + 1
        else:
            Counter[i + 1] = 0
    return Counter
text = str(input())
s = list(text)

length = len(s)
pref = pref_func(s)
print(length - pref[-1])