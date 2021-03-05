A = [str(input()) for _ in range(int(input()))]
print("Initial array:")
for i in range(len(A)-1):
    print(A[i], end=", ")
print(A[len(A)-1])
ph = 0
m = len(A[0])
for i in range(m-1,-1,-1):
    print('**********')
    ph += 1
    print("Phase",ph)
    bucket = [[] for _ in range(10)]
    for j in range(len(A)):
        bucket[ord(A[j][i]) - ord('0')].append(A[j])
    for j in range(10):
        if len(bucket[j])==0:
            print("Bucket "+str(j)+": empty")
        else:
            print("Bucket "+str(j)+": ", end='')
            for k in range(len(bucket[j])-1):
                print(bucket[j][k],end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(10):
        for k in range(len(bucket[j])):
            A[p] = bucket[j][k]
            p += 1
print('**********')
print("Sorted array:")
for i in range(len(A)-1):
    print(A[i], end=", ")
print(A[len(A)-1])