def fun(n, window, a):
    stack = []
    for i in range(window):
        while stack and a[i] <= a[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(window, n):
        print(a[stack[0]])
        while stack and i - window >= stack[0]:
            stack.pop(0)
        while stack and a[i] <= a[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(a[stack[0]])

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    fun(N, K, a)

main()