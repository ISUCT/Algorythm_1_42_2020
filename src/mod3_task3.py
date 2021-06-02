def period(c):
    a = [0] * len(c)
    for i in range(1, len(c)):
        z = a[i-1]
        while (z > 0 and c[z] != c[i]):
            z = a[z - 1]
        if c[i] == c[z]:
            z= z+1
        a[i] = z
    return a

def main():
    c = input()
    c_t = c + '&' + c
    L = period(c_t)
    lr = L[-1]-L[len(c)-1]
    z = len(c)//lr
    if c[:lr]*z == c:
        print(z)
    else:
        print(1)

main() 