def bubble_sort(k, n):
    for i in range(n):
        k[i] = list(map(int, input().split(' ')))
    for i in range(1, n):
        for j in range(n-i):
            if k[j][1] < k[j+1][1]:
                k[j],k[j+1] = k[j+1],k[j]
            elif k[j][1] == k[j+1][1] and k[j][0] > k[j+1][0]:
                    k[j],k[j+1] = k[j+1],k[j]
    for i in range(n):
        print(' '.join(map(str,k[i])))
a = int(input())
k = [1]*a
bubble_sort(k, a)





    






