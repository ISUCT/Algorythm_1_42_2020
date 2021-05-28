def fun(a, j):
    stack = [j - 1]
    n = [0] * j
    n[j - 1] = -1
    for i in range(j - 2, -1, -1):
        if a[i] <= a[stack[-1]]:
            while stack and a[stack[-1]] >= a[i]:
                stack.pop()
            if not stack:
                n[i] = -1
            else:
                n[i] = stack[-1]
            stack.append(i)
        else:
            n[i] = stack[-1]
            stack.append(i)
    return n

j = int(input())
a = list(map(int, input().split()))
a = fun(a, j)

print(" ".join(map(str, a)))