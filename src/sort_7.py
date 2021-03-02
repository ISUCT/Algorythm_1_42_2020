A = [str(input()) for _ in range(int(input()))]
print("Initial array:")
for i in range(len(A)):
    print(A[i], end=" ")
print()

m = len(A[0])
for i in range(m-1,-1,-1):
    print('**********')
    print("Phase",i)
    bucket = [[] for _ in range(10)]
    for j in range(len(A)):
        bucket[ord(A[j][i]) - ord('0')].append(A[j])
    for j in range(10):
        if len(bucket[j])==0:
            print("Bucket",j,": empty")
        else:
            print("Bucket",j,": ", end='')
            for k in bucket[j]:
                print(k,end=' ')
            print()
    p = 0
    for j in range(10):
        for k in range(len(bucket[j])):
            A[p] = bucket[j][k]
            p += 1
print('**********')
print("Sorted array:")
for i in range(len(A)):
    print(A[i], end=" ")
print()