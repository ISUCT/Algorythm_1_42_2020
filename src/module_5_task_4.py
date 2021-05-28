def build(v, l, r, segment_tree, n):
    if r - l == 1:
        segment_tree[v] = n[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segment_tree, n)
    build(2*v+2, m, r, segment_tree, n)
    segment_tree[v] = (segment_tree[2*v+1] + segment_tree[2*v+2])

def getSum(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    st_l = getSum (2*v+1, l, m, segment_tree, ql, qr)
    st_r = getSum (2*v+2, m, r, segment_tree, ql, qr)
    return st_l + st_r

def findN(v, l, r, segment_tree, n): 
    if n > segment_tree[v]: 
        return -1
    if r - l == 1:
        return r 
    m = (r+l)//2
    if segment_tree[2*v+1] >= n: 
        return findN(2*v+1, l, m, segment_tree, n)
    else: 
        return findN(2*v+2, m, r, segment_tree, n - segment_tree[2*v+1])

def main():
    a = int(input())
    num = [1 if int(i) == 0 else 0 for i in input().split()]
    segment_tree = [0]*4*a
    build(0, 0, a, segment_tree, num)
    q = int(input())
    arr = []
    while q !=0:
        l, r, n = map(int, input().split())
        sum = getSum(0, 0, a, segment_tree, l-1, r)
        if sum >= n and l == 1:
            arr.append(findN(0, 0, a, segment_tree, n))
        elif sum >= n and l > 1:
            arr.append(findN(0, 0, a, segment_tree, n +(getSum(0, 0, a, segment_tree, 0, l-1))))
        else:
            arr.append(-1)
        q -= 1
    print(*arr)

main()