
N = int(input())
m = list(map(int, input().split(" ")))
k = int(input())
t = list(map(int, input().split(" ")))
def counting_sort(m, t, n):
    temp = [0]*(n+1)
    for item in t:
        temp[item] += 1
    for i in range(n):
        if m[i] >= temp[i+1]:
            print("no")
        else:
            print("yes")

counting_sort(m, t, N)