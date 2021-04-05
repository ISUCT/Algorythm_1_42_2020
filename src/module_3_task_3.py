def prefix_fun(a):
    P = [0]*len(a)
    for i in range(len(a) - 1):
        j = P[i]
        while j > 0 and (a[i+1] != a[j]):
            j = P[j-1]
        if a[i+1] == a[j]:
            P[i+1] = j+1
        else:
            P[i+1] = 0
    return P
    
def main():
    s = input()
    s_t = s + '&' + s
    P = prefix_fun(s_t)
    pr = P[-1]-P[len(s)-1]
    k = len(s)//pr
    if s[:pr]*k == s:
        print(k)
    else:
        print(1)

main()