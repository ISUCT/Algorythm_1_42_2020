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
    t = input()
    t_s = t + '&' + s
    P = prefix_fun(t_s)
    for i in range(len(P)):
        if P[i] == len(t):
            print(i-2*len(t), end = ' ')

main()