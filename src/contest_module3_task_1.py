def hash(A, n):
    hash_str = 0
    for i in range(n):
        hash_str = (hash_str * p + ord(A[i])) % q
    return hash_str

def rabin_karp(str, sub_str, n, m):
    lst = []
    str_hash = hash(str, n)
    sub_str_hash = hash(sub_str, m)
    hash_tag = 1
    for i in range(n):
        hash_tag = (hash_tag * p) % q
    for i in range(n-m+1):
        if str_hash == sub_str_hash:
            lst.append(i)
        str_hash = (((str_hash * p - ord(str[i]) * hash_tag + ord(str[i + m - 1])) % q) + p) % p
    return lst

string = input()
sub_string = input()
global p
p = 31
global q
q = 2**31 - 1
A = rabin_karp(string, sub_string, len(string), len(sub_string))
print(' '.join(map(str, A)))