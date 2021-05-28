def fun(a):
    stack = []
    n = 0
    for i in range(len(a)):
        if (a[i] == "("): 
            stack.append(a[i])
        elif (stack!=[]) and (stack[len(stack)-1] == "("): 
            stack.pop() 
        else:
            n += 1 
    return n +len(stack)

a=input()
print(fun(a))