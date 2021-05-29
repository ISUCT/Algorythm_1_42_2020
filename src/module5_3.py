from math import gcd

def build(v, x, r, it, num): 
    if r-x == 1:
        it[v] = num[x]
        return
    m = (r+x)//2
    build(2*v+1, x, m, it, num)
    build(2*v+2, m, r, it, num)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def get_NOD(v, x, r, it, ql, qr):
    if ql <= x and qr >= r:
        return it[v]
    if ql >= r or qr <= x: 
        return 0
    m = (r+x)//2
    tl = get_NOD(2*v+1, x, m, it, ql, qr)
    tr = get_NOD(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input())
    num = list(map(int, input().split()))
    it = [0]*4*n  
    build(0, 0, n, it, num)
    q = int(input())
    index = []
    while q != 0:
        x, r = map(int, input().split())
        index.append(get_NOD(0, 0, n, it, x-1, r))
        q -= 1
    print(*index)

main()