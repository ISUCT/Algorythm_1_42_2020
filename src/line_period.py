def line_period(s):
    x = [0] * len(s)
    for i in range(1, len(s)):
        k = x[i-1]
        while (k > 0 and s[k] != s[i]):
            k = x[k - 1]
        if s[i] == s[k]:
            k += 1
        x[i] = k
    return x

def main():
    s = input()
    s_t = s + '&' + s
    L = line_period(s_t)
    lr = L[-1]-L[len(s)-1]
    k = len(s)//lr
    if s[:lr]*k == s:
        print(k)
    else:
        print(1)

main()