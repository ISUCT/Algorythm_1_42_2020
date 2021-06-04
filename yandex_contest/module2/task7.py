massiv = []
length = int(input())
for i in range(length):
    massiv.append(input())
print("Initial array:")
print(', '.join(massiv))
c = len(massiv[0])
ph=0
r=10
for i in range(c-1,-1,-1):
    ph+=1
    print('**********')
    print(f'Phase {ph}')
    b = [[] for _ in range(r)]
    for j in range(len(massiv)):
        b[ord(massiv[j][i]) - ord('0')].append(massiv[j])
    for j in range(r):
        if len(b[j])==0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(b[j])-1):
                print(b[j][now],end=', ')
            print(b[j][len(b[j])-1])
    p = 0
    for j in range(r):
        for k in range(len(b[j])):
          massiv[p] = b[j][k]
          p += 1
 
print('**********')
print("Sorted array:")
print(', '.join(massiv))