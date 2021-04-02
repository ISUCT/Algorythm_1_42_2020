def nearest_lesser(A, n):
    stack = [n-1]
    indexes = [0]*n
    indexes[n-1] = -1
    for i in range(n-2, -1, -1):
        if A[stack[-1]] >= A[i]:
            while (stack != []) and (A[stack[-1]] >= A[i]):
                stack.pop()
            if (stack == []):
                indexes[i] = -1
            else:
                indexes[i] = stack[-1]
            stack.append(i)
        else:
            indexes[i] = stack[-1]
            stack.append(i)
    return indexes
            

N = int(input())
A = list(map(int, input().split()))
A = nearest_lesser(A, N)
print(' '.join(map(str, A)))