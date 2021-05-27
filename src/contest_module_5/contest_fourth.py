def building_tree(b, lef, righ, s_tree, a):
    if righ-lef == 1:
        s_tree[b] = a[lef]
        return
    m = (righ+lef)//2
    building_tree(2*b+1, lef, m, s_tree, a)
    building_tree(2*b+2, m, righ, s_tree, a)
    s_tree[b] = s_tree[2*b+1] + s_tree[2*b+2]

def search(b, lef, righ, s_tree, k):
    if k > s_tree[b]:
        return -1
    if righ - lef == 1:
        return righ
    m = (righ+lef)//2
    if s_tree[2*b+1] >= k:
        return search(2*b+1, lef, m, s_tree, k)
    else:
        return search(2*b+2, m, righ, s_tree, k - s_tree[2*b+1])

def get_sum(b, lef, righ, s_tree, ql, qr):
    if ql <= lef and qr >= righ:
        return s_tree[b]
    if ql >= righ or qr <= lef:
        return 0
    m = (righ+lef)//2
    s_left = get_sum(2*b+1, lef, m, s_tree, ql, qr)
    s_right = get_sum(2*b+2, m, righ, s_tree, ql, qr)
    return s_left + s_right
def main():
    num = int(input())
    a = [0 if int(i) != 0 else 1 for i in input().split()]
    s_tree = [0]*4*num
    building_tree(0, 0, num, s_tree, a)
    q = int(input())
    index = []
    while q != 0:
        lef, righ, k = map(int, input().split())
        sum = get_sum(0, 0, num, s_tree, lef-1, righ)
        if sum >= k and lef > 1:
            index.append(search(0, 0, num, s_tree, k+get_sum(0, 0, num, s_tree, 0, lef-1)))
        elif sum >= k and lef == 1:
            index.append(search(0, 0, num, s_tree, k))
        else:
            index.append(-1)
        q -= 1
    print(*index)
main()