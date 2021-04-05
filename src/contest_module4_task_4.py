def range_minium(A, n, k):
    dequeue = []
    for i in range(k):
        while (dequeue != []) and (A[i] <= A[dequeue[-1]]):
            dequeue.pop()
        dequeue.append(i)
    for i in range(k, n):
        print(A[dequeue[0]])
        while (dequeue != []) and (i-k >= dequeue[0]):
            dequeue.pop(0)
        while (dequeue != []) and (A[i] <= A[dequeue[-1]]):
            dequeue.pop()
        dequeue.append(i)
    print(A[dequeue[0]])

N, K = map(int, input().split())
A = list(map(int, input().split()))
range_minium(A, N, K)