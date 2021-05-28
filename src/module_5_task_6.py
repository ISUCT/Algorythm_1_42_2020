def build(value, l, r, segments_tree, num):
    if r - l == 1:
        segments_tree[value] = num[l]
        return

    middle = (r + l) // 2
    build(2 * value + 1, l, middle, segments_tree, num)
    build(2 * value + 2, middle, r, segments_tree, num)
    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

def getKzero(value, l, r, segments_tree, num):
    if num > segments_tree[value]:
        return -1
    if r - l == 1:
        return r

    middle = (r + l) // 2

    if segments_tree[2 * value + 1] >= num:
        return getKzero(2 * value + 1, l, middle, segments_tree, num)
    else:
        return getKzero(2 * value + 2, middle, r, segments_tree, num - segments_tree[2 * value + 1])

def get_sum(value, l, r, segments_tree, q_l, q_r):
    if q_l <= l and q_r >= r:
        return segments_tree[value]
    if q_l >= r or q_r <= l:
        return 0

    middle = (r + l) // 2
    t_left = get_sum(2 * value + 1, l, middle, segments_tree, q_l, q_r)
    t_right = get_sum(2 * value + 2, middle, r, segments_tree, q_l, q_r)
    return t_left + t_right

def update(value, l, r, segments_tree, index, num):
    if r - l == 1:
        segments_tree[value] = num
        return
    middle = (r + l) // 2
    if index < middle:
        update(2 * value + 1, l, middle, segments_tree, index, num)
    else:
        update(2 * value + 2, middle, r, segments_tree, index, num)
    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

n = int(input())
number = [0 if int(i) != 0 else 1 for i in input().split()] 
segments_tree = [0] * 4 * n
build(0, 0, n, segments_tree, number)
q = int(input())

res = []
while q != 0:
    item = input().split()
    if len(item) == 4:
        l, r, num = int(item[1]), int(item[2]), int(item[3])
        sum = get_sum(0, 0, n, segments_tree, l-1, r)
        if sum >= num and l > 1:
            res.append(getKzero(0, 0, n, segments_tree, num + get_sum(0, 0, n, segments_tree, 0, l - 1)))
        elif sum >= num and l == 1:
            res.append(getKzero(0, 0, n, segments_tree, num))
        else:
            res.append(-1)
    else:
        first, second = int(item[1]), int(item[2])
        if second == 0:
            update(0, 0, n, segments_tree, first-1, 1)
        else:
            update(0, 0, n, segments_tree, first-1, 0)
    q -= 1

print(*res)