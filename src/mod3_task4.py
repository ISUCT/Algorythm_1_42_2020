def function(c):
    x = len(c)
    count = [0] * x  
    count[0] = 0
    for i in range (x - 1):
        j = count[i]
        while (j > 0) and (c[i + 1] != c[j]):
            j = count[j - 1]
        if (c[i + 1] == c[j]):
            count[i+1] = j + 1
        else:
            count[i + 1] = 0
    return count
txt = str(input())
c = list(txt)
x = len(c)
pref = function(c)
print(x - pref[-1]) 