from math import gcd

def building_tree(b, lef, righ, s_tree, a):
    if righ-lef == 1:
        s_tree[b] = a[lef]
        return
    m = (lef+righ)//2
    building_tree(2*b + 1, lef, m, s_tree, a)
    building_tree(2*b + 2, m, righ, s_tree, a)
    s_tree[b] = gcd(s_tree[2*b + 1], s_tree[2*b + 2])

def get_GCD(b, lef, righ, s_tree, q_left, q_right):
    if q_left <= lef and q_right >= righ:
        return s_tree[b]
    if q_left >= righ or q_right <= lef:
        return 0
    m = (righ+lef)//2
    s_left = get_GCD(2*b+1, lef, m, s_tree, q_left, q_right)
    s_right = get_GCD(2*b+2, m, righ, s_tree, q_left, q_right)
    return gcd(s_left, s_right)

def up(b, lef, righ, s_tree, index, val):
    if righ-lef == 1:
        s_tree[b] = val
        return
    m = (righ+lef)//2
    if index < m:
        up(2*b+1, lef, m, s_tree, index, val)
    else:
        up(2*b+2, m, righ, s_tree, index, val)
    s_tree[b] = gcd(s_tree[2*b + 1], s_tree[2*b + 2])

def main():
    nums = int(input())
    seg_tree = [0]*4*nums
    a = list(map(int, input().split()))[:nums]
    building_tree(0, 0, nums, seg_tree, a)
    q = int(input())
    result = []
    while q != 0:
        que, l, r = map(str, input().split())
        if que=="s":
            result.append(get_GCD(0, 0, nums, seg_tree, int(l)-1, int(r)))
        else:
            up(0, 0, nums, seg_tree, int(l)-1, int(r))
        q -= 1
    print(*result)
main() 