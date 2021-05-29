length = int(input())
traject_a = list(map(int,input().split()))
traject_b = []
stack = []
test =  sorted(traject_a)
for i in range(length):
    if (stack == []) or (stack[-1] > traject_a[0]):
        stack.append(traject_a[0])
        traject_a.pop(0)
    else:
        while (stack != [] and stack[-1] < traject_a[0]):
            traject_b.append(stack[-1])
            stack.pop(-1)
        if (stack == []) or (stack[-1] > traject_a[0]):
            stack.append(traject_a[0])
            traject_a.pop(0)        
if stack != []: 
    for i in range(len(stack)):
        traject_b.append(stack[-1])
        stack.pop(-1)   
if traject_b == test:
    print("YES")
else: 
    print("NO") 