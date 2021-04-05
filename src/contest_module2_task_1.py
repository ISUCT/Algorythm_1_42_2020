N = int(input())
array = ""
array = input()
A = array.split(" ")

num_swap = 0
for i in range(0, N):
    for j in range(0, N-i-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
            num_swap += 1
            print(" ".join(map(str,A)))
if num_swap == 0:
    print (0)