def sub_din(val, x, r, s_sub, p):
    if r-x == 1:
        s_sub[val] = p[x]
        return
    m = (r+x)//2
    sub_din(2*val+1, x, m, s_sub, p)
    sub_din(2*val+2, m, r, s_sub, p)
    s_sub[val] = s_sub[2*val+1] + s_sub[2*val+2]

def search(val, x, r, s_sub, t):
    if t > s_sub[val]:
        return -1
    if r - x == 1:
        return r
    m = (r+x)//2
    if s_sub[2*val+1] >= t:
        return search(2*val+1, x, m, s_sub, t)
    else:
        return search(2*val+2, m, r, s_sub, t - s_sub[2*val+1])

def get_sum(val, x, r, s_sub, qx, qr):
    if qx <= x and qr >= r:
        return s_sub[val]
    if qx >= r or qr <= x:
        return 0
    m = (r+x)//2
    tx = get_sum(2*val+1, x, m, s_sub, qx, qr)
    tr = get_sum(2*val+2, m, r, s_sub, qx, qr)
    return tx + tr

def up(val, x, r, s_sub, indx, value):
    if r-x == 1:
        s_sub[val] = value
        return
    m = (r+x)//2
    if indx < m:
        up(2*val+1, x, m, s_sub, indx, value)
    else:
        up(2*val+2, m, r, s_sub, indx, value)
    s_sub[val] = s_sub[2*val+1] + s_sub[2*val+2]
def main():
    n = int(input())
    p = [0 if int(i) != 0 else 1 for i in input().split()]
    s_sub = [0]*4*n
    sub_din(0, 0, n, s_sub, p)
    q = int(input())
    ind = []
    while q != 0:
        i = input().split()
        if len(i) == 4:
            x, r, t = int(i[1]), int(i[2]), int(i[3])
            cout_ = get_sum(0, 0, n, s_sub, x-1, r)
            if cout_ >= t and x > 1:
                ind.append(search(0, 0, n, s_sub, t+get_sum(0, 0, n, s_sub, 0, x-1)))
            elif cout_ >= t and x == 1:
                ind.append(search(0, 0, n, s_sub, t))
            else:
                ind.append(-1)
        else:
            i, val = int(i[1]), int(i[2])
            if val == 0:
                up(0, 0, n, s_sub, i-1, 1)
            else:
                up(0, 0, n, s_sub, i-1, 0)
        q -= 1
    print(*ind)
main()