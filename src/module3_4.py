def pref_funct(s,n):
    k = [0] * n    
    k[0] = 0
    for i in range (n - 1):
        j = k[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = k[j - 1]
        if (s[i + 1] == s[j]):
            k[i+1] = j + 1
        else:
            K[i + 1] = 0
    return k
#префикс функция  

A = input()
n = len(A)
pref = pref_funct(A,n)
print(n - pref[-1])