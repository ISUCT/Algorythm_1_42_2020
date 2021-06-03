def poezd_sort(A, n):
    stack = []
    B = [] 
    poezd_sorted = sorted(A)
    while(len(B) != n):
        if (stack == []):
            stack.append(A[0])
            A.pop(0)
            continue   
        if (len(A) > 0) and (A[0] <= stack[-1]):
            stack.append(A[0])
            A.pop(0)
        else:
            B.append(stack[-1])
            stack.pop()
    return B == poezd_sorted

N = int(input())
poezd = list(map(int, input().split()))
if poezd_sort(poezd, N):
    print("YES")
else:
    print("NO")