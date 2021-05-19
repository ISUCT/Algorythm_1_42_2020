def play_station_portable(s):
    k = 0
    massiv = []
    for i in s:
        if (i == '('):
            massiv.append(i)
        elif (massiv != []) and (massiv[-1] == '('):
            massiv.pop()
        else:
            k += 1
    return k+len(massiv)

s = str(input())
print(play_station_portable(s)) 