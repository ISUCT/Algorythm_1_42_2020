def building_tree(x, lef, righ, s_tree, a):
    if righ-lef == 1:
        s_tree[x] = a[lef]
        return
    m = (righ+lef)//2
    building_tree(2*x+1, lef, m, s_tree, a)
    building_tree(2*x+2, m, righ, s_tree, a)
    s_tree[x] = s_tree[2*x+1] + s_tree[2*x+2]

def search(x, lef, righ, s_tree, k):
    if k > s_tree[x]:
        return -1
    if righ - lef == 1:
        return righ
    m = (righ+lef)//2
    if s_tree[2*x+1] >= k:
        return search(2*x+1, lef, m, s_tree, k)
    else:
        return search(2*x+2, m, righ, s_tree, k - s_tree[2*x+1])

def get_sum(x, lef, righ, s_tree, left, right):
    if left <= lef and right >= righ:
        return s_tree[x]
    if left >= righ or right <= lef:
        return 0
    m = (righ+lef)//2
    t_left = get_sum(2*x+1, lef, m, s_tree, left, right)
    t_right = get_sum(2*x+2, m, righ, s_tree, left, right)
    return t_left + t_right

def up(x, lef, righ, s_tree, ind_new, value):
    if righ-lef == 1:
        s_tree[x] = value
        return
    m = (righ+lef)//2
    if ind_new < m:
        up(2*x+1, lef, m, s_tree, ind_new, value)
    else:
        up(2*x+2, m, righ, s_tree, ind_new, value)
    s_tree[x] = s_tree[2*x+1] + s_tree[2*x+2]
def main():
    n = int(input())
    a = [0 if int(i) != 0 else 1 for i in input().split()]
    s_tree = [0]*4*n
    building_tree(0, 0, n, s_tree, a)
    q = int(input())
    index = []
    while q != 0:
        i = input().split()
        if len(i) == 4:
            lef, righ, k = int(i[1]), int(i[2]), int(i[3])
            summ = get_sum(0, 0, n, s_tree, lef-1, righ)
            if summ >= k and lef > 1:
                index.append(search(0, 0, n, s_tree, k+get_sum(0, 0, n, s_tree, 0, lef-1)))
            elif summ >= k and lef == 1:
                index.append(search(0, 0, n, s_tree, k))
            else:
                index.append(-1)
        else:
            i, x = int(i[1]), int(i[2])
            if x == 0:
                up(0, 0, n, s_tree, i-1, 1)
            else:
                up(0, 0, n, s_tree, i-1, 0)
        q -= 1
    print(*index)
main() 