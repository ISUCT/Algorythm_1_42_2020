m = [[int(i) for i in input().split(" ")]for _ in range(int(input("Введите количество строк")))]
c = 0
i = 0
while 1:
    if m[i][1] < m[i+1][1]:
        m[i],m[i+1] = m[i+1],m[i]
        c += 1
    elif m[i][1] = m[i+1][1] and m[i][0] > m[i+1][0]:
        m[i],m[i+1] = m[i+1],m[i]
        c += 1
    

