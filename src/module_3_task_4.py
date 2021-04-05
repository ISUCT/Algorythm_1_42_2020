def prefix_fun(a, k):
    P = [0]*k
    P[0] = 0
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
    k = len(s)
    P = prefix_fun(s, k)   
    print(len(s) - P[len(P)-1])

main()