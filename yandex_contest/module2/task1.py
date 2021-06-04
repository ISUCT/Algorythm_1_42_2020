a = int(input())
stroka = input()
new_stroka = stroka.split(" ")
massiv = []
for i in range(0, len(stroka)):
    massiv.append(int(new_stroka[i]))
n = len(stroka)
num = 0
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if massiv[j] > massiv[j+1]:
            massiv[j], massiv[j+1] = massiv[j+1], massiv[j]
            num += 1
            print(" ".join(map(str, massiv)))
if num == 0:
    print(0)
