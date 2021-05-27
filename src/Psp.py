def Psp(s):
    Counter=0
    myStack = []
    for c in s:
        if (c == '('):
            myStack.append(c)
        elif (myStack != []) and (myStack[-1] == '('):
            myStack.pop()
        else:
            Counter += 1
    return Counter+len(myStack)

s = str(input())
print(Psp(s))