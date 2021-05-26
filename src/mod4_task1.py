def psp(c):
    Counter = 0
    mass = []
    for i in c:
        if (i == '('):
            mass.append(i)
        elif (mass != []) and (mass[-1] == '('):
            mass.pop()
        else:
            Counter= Counter+1
    return Counter+len(mass)

c = str(input())
print(psp(c)) 