def g_c_f(b, lft, rght, s_leaf, arr):
    if rght - lft == 1:
        s_leaf[b] = arr[lft]
        return
    m = (rght + lft) // 2
    g_c_f(2 * b + 1, lft, m, s_leaf, arr)
    g_c_f(2 * b + 2, m, rght, s_leaf, arr)
    s_leaf[b] = GCF(s_leaf[2 * b + 1], s_leaf[2 * b + 2])
    
def GCF(p,b):
    while b:
        p, b = b, p%b
    return p
    
def get_GCF(b, lft, rght, s_leaf, left, right):
    if left <= lft and right >= rght:
        return s_leaf[b]
    if left >= rght or right <= lft:
        return 0
    m = (rght + lft) // 2
    st_right = get_GCF(2 * b + 2, m, rght, s_leaf, left, right)
    st_left = get_GCF(2 * b + 1, lft, m, s_leaf, left, right)
    return GCF(st_left, st_right)
    

def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    s_leaf = [0] * 4 * n 
    g_c_f(0, 0, n, s_leaf, arr)
    q = int(input())
    p = []

    while q != 0:
        lft, rght = map(int, input().split())
        p.append(get_GCF(0, 0, n, s_leaf, lft - 1, rght))
        q -= 1
    print(*p)

main()