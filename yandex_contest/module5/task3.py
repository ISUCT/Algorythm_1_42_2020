from math import gcd
def bld(v, l, r, segment_tree, nums):
    if r - l == 1:
        segment_tree[v] = nums[l]
        return
    m = (r+l)//2
    bld(2*v+1, l, m, segment_tree, nums)
    bld(2 * v + 2, m, r, segment_tree, nums)
    segment_tree[v] = gcd(segment_tree[2*v +1], segment_tree[2*v + 2])


def nod(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = int(nod(2*v +1, l, m, segment_tree, ql, qr))
    st_r = int(nod(2*v + 2, m, r, segment_tree, ql, qr))
    return gcd(st_l, st_r)




n = int(input())
numbers = list(map(int, input().split()))[:n]
segment_tree = [0]*4*n
bld(0, 0, n, segment_tree, numbers)
q = int(input())
massiv = []
while q != 0:
    l, r = map(int, input().split())
    massiv.append(int(nod(0, 0, n, segment_tree, l-1, r)))
    q -= 1
print(*massiv)


