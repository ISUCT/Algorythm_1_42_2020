print("Введите список", " ")
n = int(input())
s = False
mas = list(map(int,input().split()))
print("Методом пузырьковой сортировки получаем : ", " ")
for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            s = True
            mas[i], mas[i+1] = mas[i+1], mas[i]
            for i in mas:
                print(i, end = ' ')
            print()
if s != True:
    print(0)
