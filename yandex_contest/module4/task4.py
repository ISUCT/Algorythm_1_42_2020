from collections import deque
n,k= map(int,input().split())
numbers=list(map(int,input().split()))
dq=deque()
for i in range(k):
  while dq and numbers[i] < numbers[dq[-1]]:
    dq.pop()
  dq.append(i)
print(numbers[dq[0]])
for i in range(k,n):
  while dq and dq[0] <=i-k:
    dq.popleft()
  while dq and numbers[i] <= numbers[dq[-1]]:
    dq.pop()
  dq.append(i)
  print(numbers[dq[0]])