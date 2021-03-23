def hash(A, n):
    hash_str = 0
    for i in range(n):
        hash_str = (hash_str * p + ord(A[i])) % q
    return hash_str

def rabin_karp(s, t, n):
    s_hash = hash(s, n)
    t_hash = hash(t, n)
    pt = 1
    for i in range(n-1):
        pt = (pt * p) % q
    if s_hash == t_hash:
        return 0
    for i in range(n-1):
        t_hash = (t_hash - ord(t[i]) * pt) * p
        t_hash += ord(t[i])
        t_hash %= q       
        if s_hash == t_hash:
            return i+1
    return -1 

S = input()
T = input()
global p
p = 31
global q
q = 2 ** 31 - 1
A = rabin_karp(S, T, len(S))
print(A)