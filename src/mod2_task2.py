n= int(input())
s=[]
for i in range (n): 
    s.append(input().split(" "))
s=[[int(s[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range (n-1-i):
        if  s[j][1]<s[j+1][1]:
            t = s[j+1]
            s[j+1] = s[j]
            s[j] = t
        if  s[j][1]==s[j+1][1] and s[j][0]>s[j+1][0]:
            t = s[j+1]
            s[j+1] = s[j]
            s[j] = t
                 
[print(i[0], i[1]) for i in s]