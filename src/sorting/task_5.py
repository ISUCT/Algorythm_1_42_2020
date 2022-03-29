def counting_sort(M, n):
    max = -2e9 - 1
    total = 0
    for item in M:
        if abs(item) > max:
            max = abs(item)
    arr = [0]*(max+1)
    for i in range(0, n):
        temp = M[i]    
        if temp >=0:
            if arr[abs(temp)] != 3:
                arr[abs(temp)] += 1
                if arr[abs(temp)] > 1 and arr[abs(temp)] != 5:
                    arr[abs(temp)] -= 1
        else:
            if arr[-temp] == 1:
                arr[-temp] = 3
            elif arr[-temp] == 0:
                arr[-temp] += 4

    for i in range(0, abs(max)+1):
        if arr[i] == 1 or arr[i] == 4:
            total +=1
        elif arr[i] == 3 or arr[i] == 5:
            total += 2

    return total

N = int(input())
M = list(map(int, input().split(" ")))
print(counting_sort(M, N))