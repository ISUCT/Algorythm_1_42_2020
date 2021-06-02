def subsegment(b, lft, rght, s_sub, p):
    if rght-lft == 1:
        s_sub[b] = p[lft]
        return
    m = (rght+lft)//2
    subsegment(2*b+1, lft, m, s_sub, p)
    subsegment(2*b+2, m, rght, s_sub, p)
    s_sub[b] = s_sub[2*b+1] + s_sub[2*b+2]

def rummage(b, lft, rght, s_sub, t):
    if t > s_sub[b]:
        return -1
    if rght - lft == 1:
        return rght
    m = (rght+lft)//2
    if s_sub[2*b+1] >= t:
        return rummage(2*b+1, lft, m, s_sub, t)
    else:
        return rummage(2*b+2, m, rght, s_sub, t - s_sub[2*b+1])

def get_sum(b, lft, rght, s_sub, ql, qr):
    if ql <= lft and qr >= rght:
        return s_sub[b]
    if ql >= rght or qr <= lft:
        return 0
    m = (rght+lft)//2
    s_left = get_sum(2*b+1, lft, m, s_sub, ql, qr)
    s_right = get_sum(2*b+2, m, rght, s_sub, ql, qr)
    return s_left + s_right
def main():
    arr = int(input())
    p = [0 if int(i) != 0 else 1 for i in input().split()]
    s_sub = [0]*4*arr
    subsegment(0, 0, arr, s_sub, p)
    q = int(input())
    index = []
    while q != 0:
        lft, rght, t = map(int, input().split())
        sum = get_sum(0, 0, arr, s_sub, lft-1, rght)
        if sum >= t and lft > 1:
            index.append(rummage(0, 0, arr, s_sub, t+get_sum(0, 0, arr, s_sub, 0, lft-1)))
        elif sum >= t and lft == 1:
            index.append(rummage(0, 0, arr, s_sub, t))
        else:
            index.append(-1)
        q -= 1
    print(*index)
main()