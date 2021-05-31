def store(D, k):
    digit = len(D[0])
    for c in range(digit):
        mass = [[] for f in range(10)]
        for item in D:
            index = int(item)//10**c % 10
            mass[index].append(item)
        print("Phase", c+1)
        D = []
        for c in range(10):
            print("Bucket ", c ,":", sep = "", end=" ")
            print(", ".join(mass[c]) if len(mass[c])>0 else "empty")
            D += mass[c]
        print("**********")
    return D
 
k = int(input())
D = []
for i in range(k):
    D.append(input())
print("Initial array:")
print(", ".join(D))
print("**********")
D = store(D, k)
print("Sorted array:")
print(", ".join(D))