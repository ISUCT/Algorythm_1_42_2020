n = int(input())
m = [[int(i) for i in input().split(" ")] for _ in range(n)]
i = 0
c = 0 
while 1:
	if m[i][1] < m[i+1][1]:
		m[i],m[i+1] = m[i+1],m[i]
		c += 1
	elif m[i][1] == m[i+1][1] and m[i][0] > m[i+1][0]:
		m[i],m[i+1] = m[i+1],m[i]
		c += 1
	if c == 0 and i == n - 2:
		break
	elif i == n - 2:
		i = -1
		c = 0
	i += 1
for i in range(n):
	print(m[i][0],m[i][1])
