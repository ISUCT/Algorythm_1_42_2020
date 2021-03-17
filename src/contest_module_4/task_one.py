def PSP(s):
    Counter = 0
    my_list = []
    for i in s:
        if (i == '('):
            my_list.append(i)
        elif (my_list != []) and (my_list[-1] == '('):
            my_list.pop()
        else:
            Counter += 1
    return Counter+len(my_list)

s = str(input())
print(PSP(s))