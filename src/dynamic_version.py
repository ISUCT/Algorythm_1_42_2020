from math import gcd

def dynamic_version(val, x, r, num, p): 
    if r - x == 1:
        num[val] = p[x]
        return

    middle = (x + r)//2
    dynamic_version(2*val + 1, x, middle, num, p)
    dynamic_version(2*val + 2, middle, r, num, p)
    num[val] = gcd(num[2*val+1], num[2*val+2])    

def calc(val, x, r, it, q_x, q_r): 
    if q_x <= x and q_r >= r:
        return it[val]
    if q_x >= r or q_r <= x:
        return 0

    middle = (x + r)//2
    tx = calc(2*val + 1, x, middle, it, q_x, q_r)
    tr = calc(2*val + 2, middle, r, it, q_x, q_r)
    return gcd(tx, tr) 

def up(val, x, r, num, idx, value):
    if r - x == 1:
        num[val] = value
        return
    middle = (r+x)//2
    if idx < middle: 
        up(val*2+1, x, middle, num, idx, value)
    else:
        up(val*2+2, middle, r, num, idx, value)
    num[val] = gcd(num[2*val+1], num[2*val+2]) 

def main(): 
    t = int(input())
    num = [0] * (4 * t)
    p = list(map(int, input().split()))[:t]
    dynamic_version(0, 0, t, num, p)
    q = int(input())
    ct = []
    while q != 0: 
        t_q, x, r = map(str, input().split())
        if t_q == 's':
            ct.append(calc(0, 0, t, num, int(x)-1, int(r)))
        else:
            up(0, 0, t, num, int(x)-1, int(r))
        q -= 1
    print(*ct)
main()