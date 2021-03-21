length = int(input())
tr_a = list(map(int,input().split()))
tr_b = []
stack = []
test =  sorted(tr_a)
for i in range(length):
    if (stack == []) or (stack[-1] > tr_a[0]):
        stack.append(tr_a[0])
        tr_a.pop(0)
    else:
        while (stack != [] and stack[-1] < tr_a[0]):
            tr_b.append(stack[-1])
            stack.pop(-1)
        if (stack == []) or (stack[-1] > tr_a[0]):
            stack.append(tr_a[0])
            tr_a.pop(0)        
if stack != []: 
    for i in range(len(stack)):
        tr_b.append(stack[-1])
        stack.pop(-1)   
if tr_b == test:
    print("YES")
else: 
    print("NO")