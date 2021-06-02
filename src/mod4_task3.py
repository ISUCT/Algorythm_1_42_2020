def close(C, p):
    stk = [p-1]
    index = [0]*p
    index[p-1] = -1
    for i in range(p-2, -1, -1):
        if C[stk[-1]] >= C[i]:
            while (stk != []) and (C[stk[-1]] >= C[i]):
                stk.pop()
            if (stk == []):
                index[i] = -1
            else:
                index[i] = stk[-1]
            stk.append(i)
        else:
            index[i] = stk[-1]
            stk.append(i)
    return index


N = int(input())
C = list(map(int, input().split()))
C = close(C, N)
print(' '.join(map(str, C))) 