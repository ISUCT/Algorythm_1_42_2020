def shift(string_two, string_one, q):
 
    if string_one == string_two: 
        return 0
 
    string_one += string_one
 
    p = 11
    m = 1
    s1hash = 0
    for i in string_two[::-1]:
        s1hash += ord(i) * m
        m *= p
        s1hash %= q
        m %= q
 
    m = 1
    hash = 0
    for i in string_one[:len(string_two)][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= q
        m %= q
 
    hashtag = 1
    for i in range(len(string_two) - 1):
        hashtag *= p
        hashtag %= q
    for i in range(1, len(string_one) - len(string_two) + 1):
        hashnew = ((hash % q - ord(string_one[i - 1]) * hashtag % q) * p % q + ord(string_one[i + len(string_two) - 1])) % q
        if hashnew == s1hash:
            return i
        hash = hashnew

    return -1
 
string_one = input()
string_two = input()
q = 2 ** 31 - 1
print(shift(string_one, string_two, q))