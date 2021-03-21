def taskseven(C, x):
    digit = len(C[0])
    for i in range(digit):
        mass = [[] for j in range(10)]
        for item in C:
            index = int(item)//10**i % 10
            mass[index].append(item)
        print("Phase", i+1)
        C = []
        for i in range(10):
            print("Bucket ", i ,":", sep = "", end=" ")
            print(", ".join(mass[i]) if len(mass[i])>0 else "empty")
            C += mass[i]
        print("**********")
    return C

x = int(input())
C = []
for i in range(x):
    C.append(input())
print("Initial array:")
print(", ".join(C))
print("**********")
C = taskseven(C, x)
print("Sorted array:")
print(", ".join(C))