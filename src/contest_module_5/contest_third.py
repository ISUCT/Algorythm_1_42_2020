def building_tree(b, lef, righ, s_three, num):
    if righ - lef == 1:
        s_three[b] = num[lef]
        return
    m = (righ + lef) // 2
    building_tree(2 * b + 1, lef, m, s_three, num)
    building_tree(2 * b + 2, m, righ, s_three, num)
    s_three[b] = NOD(s_three[2 * b + 1], s_three[2 * b + 2])

def NOD(a,b):
    while b:
        a, b = b, a%b
    return a

def get_NOD(b, lef, righ, s_three, left, right):
    if left <= lef and right >= righ:
        return s_three[b]
    if left >= righ or right <= lef:
        return 0
    m = (righ + lef) // 2
    st_left = get_NOD(2 * b + 1, lef, m, s_three, left, right)
    st_right = get_NOD(2 * b + 2, m, righ, s_three, left, right)
    return NOD(st_left, st_right)

def main():
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    s_three = [0] * 4 * n 
    building_tree(0, 0, n, s_three, nums)
    q = int(input())
    a = []

    while q != 0:
        lef, righ = map(int, input().split())
        a.append(get_NOD(0, 0, n, s_three, lef - 1, righ))
        q -= 1
    print(*a)

main()