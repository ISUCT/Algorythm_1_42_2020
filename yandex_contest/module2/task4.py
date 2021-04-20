def inv(massiv, c):

    if len(M) > 1:
        mid = len(massiv)//2
        left = massiv[:mid]
        right = massiv[mid:]
        
        c = inv(left, c)
        c = inv(right, c)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                massiv[k] = left[i]
                i += 1
            else:
                massiv[k] = right[j]
                j = j+1
                c += len(left)-i
            k = k+1
        while i < len(left):
            massiv[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            massiv[k] = right[j]
            j = j+1
            k = k+1

    return c


inversions = 0
n = int(input())
M = list(map(int, input().split()))[:n]
inversions = inv(M, inversions)
print(inversions)