def build(v, l, r, it, num):
    if r - l == 1:
        it[v] = num[l]
        return
    
    middle = (r+l)//2
    build(2*v + 1, l, middle, it, num)
    build(2*v + 2, middle, r, it, num)
    it[v] = nod(it[2*v+1], it[2*v+2])


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def get_nod(v, l, r, it, q_l, q_r):
    if q_l <= l and q_r >= r:
        return it[v]
    if q_l >= r or q_r <= l:
        return 0
    middle = (r+l)//2
    tl = get_nod(2*v + 1, l, middle, it, q_l, q_r)
    tr = get_nod(2*v + 2, middle, r, it, q_l, q_r)
    return nod(tl, tr)


def main():
    a = int(input())
    num = list(map(int, input().split()))
    it = [0] * 4 * a
    build(0, 0, a, it, num)
    q = int(input())
    idx = []
    while q != 0:
        l, r = map(int, input().split())
        idx.append(get_nod(0, 0, a, it, l-1, r))
        q -= 1
    print(*idx)

main()