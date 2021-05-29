def Segment_minima(n, m_w, s):
    stack = []
    for i in range(m_w):
        while stack and s[i] <= s[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(m_w, n):
        print(s[stack[0]])
        while stack and i - m_w >= stack[0]:
            stack.pop(0)
        while stack and s[i] <= s[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(s[stack[0]])
N, K = map(int, input().split())
s = list(map(int, input().split()))
Segment_minima(N, K, s)