def counting_sort(A, B, n):
    temp = [0]*(n+1)
    for item in B:
        temp[item] += 1
    for i in range(n):
        if A[i] >= temp[i+1]:
            print("no")
        else:
            print("yes")

N = int(input())
A = list(map(int, input().split(" ")))
k = int(input())
B = list(map(int, input().split(" ")))

counting_sort(A, B, N)