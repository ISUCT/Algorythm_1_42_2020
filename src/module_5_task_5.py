from math import gcd

def build(v, l, r, it, a): 
    if r - l == 1:
        it[v] = a[l]
        return
   
    middle = (l + r)//2
    build(2*v + 1, l, middle, it, a)
    build(2*v + 2, middle, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    

def calc(v, l, r, it, q_l, q_r): 
    if q_l <= l and q_r >= r:
        return it[v]
    if q_l >= r or q_r <= l:
        return 0
    
    middle = (l + r)//2
    tl = calc(2*v + 1, l, middle, it, q_l, q_r)
    tr = calc(2*v + 2, middle, r, it, q_l, q_r)
    return gcd(tl, tr) 

def update(v, l, r, it, idx, value):
    if r - l == 1:
        it[v] = value
        return
    middle = (r+l)//2
    if idx < middle: 
        update(v*2+1, l, middle, it, idx, value)
    else:
        update(v*2+2, middle, r, it, idx, value)
    it[v] = gcd(it[2*v+1], it[2*v+2]) 

def main(): 
    k = int(input())
    it = [0] * (4 * k)
    a = list(map(int, input().split()))[:k]
    build(0, 0, k, it, a)
    q = int(input())
    res = []
    while q != 0: 
        t_q, l, r = map(str, input().split())
        if t_q == 's':
            res.append(calc(0, 0, k, it, int(l)-1, int(r)))
        else:
            update(0, 0, k, it, int(l)-1, int(r))
        q -= 1
    print(*res)
main()