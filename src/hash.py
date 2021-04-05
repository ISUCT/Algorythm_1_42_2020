def substring_search(S, T):
    substring_str = 0
    for i in range(T):
        substring_str = (substring_str * p + ord(S[i])) % q
    return substring_str

def Rabin_Karp_Matcher(str_substring, pattern, x, y):
    lst = []
    str_substring = hash(y)
    pattern_substring = hash(y)
    pt = 1
    for i in range(x-1):
        pt = (pt * p) % q
    for i in range(1, x-y+2):
        if str_substring == pattern_substring:
            lst.append(i-1)
        if i < x-y+1:        
            str_substring = (str_substring - ord(str_substring[i-1]) * pt) * p
            str_substring += ord(str_substring[i + y - 1])
            str_substring %= q
    return lst
string = input()
pattern_string = input()
global p
p = 31
global q
q = 2 ** 31 - 1
A = Rabin_Karp_Matcher(string, pattern_string, len(string), len(pattern_string))
print(' '.join(map(str, A)))