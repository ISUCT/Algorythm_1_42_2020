def looped_string(S, n):
    res = [0]*n
    res[0] = 0
    for i in range(n-1):
        x = res[i]
        while (x > 0 and S[i+1] != S[x]):
            x = res[x-1]
        if (S[i+1] == S[x]):
            res[i+1] = x + 1
        else:
            res[i+1] = 0
    return res

T = input()
S = looped_string(T, len(T))
print(len(T) - S[len(S)-1])