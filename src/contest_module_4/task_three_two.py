#10
#1 2 3 2 1 4 2 5 3 1
#-1 4 3 4 -1 6 9 8 9 -1 

l = int(input())
a = list(zip(list(map(int, input().split())), range(l)))
stack = []
result = [0]*l
for i in reversed(a):
    while (stack != []) and (stack[-1][0] >= i[0]):
        stack.pop()
    if stack == []:
        result[i[1]] = -1
    else:
        result[i[1]] = stack[-1][1]
    stack.append(i)
print(' '.join(map(str, result)))    