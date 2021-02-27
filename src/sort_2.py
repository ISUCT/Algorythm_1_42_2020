m = [[int(i) for i in input().split(" ")] for _ in range(int(input()))]
i = 0
c = 0
while len(m)-1:
	if m[i][1] < m[i+1][1] or m[i][1] == m[i+1][1] and m[i][0] > m[i+1][0]:
		m[i],m[i+1] = m[i+1],m[i]
		c += 1
	if c == 0 and i == len(m) - 2:
		break
	elif i == len(m) - 2:
		i = -1
		c = 0
	i += 1
for i in range(len(m)):
	print(m[i][0], m[i][1])
