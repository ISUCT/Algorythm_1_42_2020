def prefix_func(string, length):
    cnt = [0] * length 
    for i in range (length - 1):
        j = cnt[i]
        while (j > 0) and (string[i + 1] != string[j]):
            j = cnt[j - 1]
        if (string[i + 1] == string[j]):
            cnt[i+1] = j + 1
        else:
            cnt[i + 1] = 0
    return cnt

s = str(input())
length = len(s)
result = prefix_func(s, length)
print(length - result[-1])
