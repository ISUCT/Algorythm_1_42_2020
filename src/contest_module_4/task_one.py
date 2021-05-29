def PSP(a):
    Count = 0
    my_list = []
    for i in a:
        if (i == '('):
            my_list.append(i)
        elif (my_list != []) and (my_list[-1] == '('):
            my_list.pop()
        else:
            Count += 1
    return Count+len(my_list)

a = str(input())
print(PSP(a))