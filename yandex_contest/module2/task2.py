a = int(input())
nabor = []
for i in range(a):
    nabor.append(list(map(int, input().split())))

for i in range(a-1):
    for j in range(a - i - 1):
        if nabor[j][1] < nabor[j+1][1]:
            nabor[j], nabor[j+1] = nabor[j+1], nabor[j]
for i in range(a-1):
    for j in range(a - i - 1):
        if nabor[j][1] == nabor[j+1][1]:
            if nabor[j][0] > nabor[j+1][0]:
                nabor[j], nabor[j+1] = nabor[j+1], nabor[j]


for i in range(a):
    stroka = ""
    stroka += str(nabor[i][0])
    for j in range(1, len(nabor[i])):
        stroka += " "
        stroka += str(nabor[i][j])
    print(stroka)
