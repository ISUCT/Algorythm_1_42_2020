def closest_smaller(S, n):
    stack = [n-1]
    index = [0]*n
    index[n-1] = -1
    for i in range(n-2, -1, -1):
        if S[stack[-1]] >= S[i]:
            while (stack != []) and (S[stack[-1]] >= S[i]):
                stack.pop()
            if (stack == []):
                index[i] = -1
            else:
                index[i] = stack[-1]
            stack.append(i)
        else:
            index[i] = stack[-1]
            stack.append(i)
    return index


N = int(input())
S = list(map(int, input().split()))
S = closest_smaller(S, N)
print(' '.join(map(str, S)))