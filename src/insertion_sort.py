
mas = [[int(i) for i in input().split(" ")]for _ in range(int(input()))]


for j in range( len(mas)):
    for i in range( len(mas)-1):
        if(mas[i][1] < mas[i+1][1]):
            mas[i][0],mas[i+1][0] = mas[i+1][0],mas[i][0]
            mas[i][1],mas[i+1][1] = mas[i+1][1],mas[i][1]
        if(mas[i][1] == mas[i+1][1]):
            if(mas[i][0] > mas[i+1][0]):
                mas[i][0],mas[i+1][0] = mas[i+1][0],mas[i][0]
                mas[i][1],mas[i+1][1] = mas[i+1][1],mas[i][1]
for i in range( len(mas)):    

        print(mas[i][0], mas[i][1])
