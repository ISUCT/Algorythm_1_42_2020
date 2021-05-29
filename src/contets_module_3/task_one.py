def getHash(fullstring, substring,c):
    a = 31
    b = 1
    s1hash = 0

    for i in substring[::-1]:
        s1hash += ord(i) * b
        b *= a
        s1hash %= c
        b %= c
    
    b = 1
    hash = 0
    for i in fullstring[:len(substring)][::-1]:
        hash += b * ord(i)
        b *= a
        hash %= c
        b %= c
    
    hashtag = 1
    for i in range(len(substring) - 1):
        hashtag *= a
        hashtag %= c
    
    List = []
    if hash == s1hash: List.append(0)
    for i in range(1, len(fullstring) - len(substring) + 1):
        hashnew = ((hash % c - ord(fullstring[i - 1]) * hashtag % c) * append % c + ord(fullstring[i + len(substring) - 1])) % q
        if hashnew == s1hash: 
            List.append(i)
        hash = hashnew
    return List

fullstring = str(input())
substring = str(input())
c = 2 ** 31 - 1
A = getHash(fullstring,substring,c)
print(' '.join(map(str, A)))
print(*A, sep=' ')
