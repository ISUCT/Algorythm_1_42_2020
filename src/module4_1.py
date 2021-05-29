def PSP(s):
    Meter = 0
    new_list = []
    for i in s:
        if (i == '('):
            new_list.append(i)
        elif (new_list != []) and (new_list[-1] == '('):
            new_list.pop()
        else:
            Meter += 1
    return Meter+len(new_list)

s = str(input())
print(PSP(s)) 