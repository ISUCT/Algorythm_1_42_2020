def min_segment(p, m_w, c):
    mass = []
    for i in range(m_w):
        while mass and c[i] <= c[mass[-1]]:
            mass.pop()
        mass.append(i)
    for i in range(m_w, p):
        print(c[mass[0]])
        while mass and i - m_w >= mass[0]:
            mass.pop(0)
        while mass and c[i] <= c[mass[-1]]:
            mass.pop()
        mass.append(i)
    print(c[mass[0]])
N, K = map(int, input().split())
c = list(map(int, input().split()))
min_segment(N, K, c) 