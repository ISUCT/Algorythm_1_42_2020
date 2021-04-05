def hash(A, n):
    hash_str = 0
    for i in range(n):
        hash_str = (hash_str * p + ord(A[i])) % q
    return hash_str

def rabin_karp(str, sub_str, n, m):
    lst = []
    str_hash = hash(str, m)
    sub_str_hash = hash(sub_str, m)
    pt = 1
    for i in range(m-1):
        pt = (pt * p) % q
    for i in range(1, n-m+2):
        if str_hash == sub_str_hash:
            lst.append(i-1)
        if i < n-m+1:        
            str_hash = (str_hash - ord(str[i-1]) * pt) * p
            str_hash += ord(str[i + m - 1])
            str_hash %= q
    return lst

string = input()
sub_string = input()
global p
p = 31
global q
q = 2 ** 31 - 1
A = rabin_karp(string, sub_string, len(string), len(sub_string))
print(' '.join(map(str, A)))