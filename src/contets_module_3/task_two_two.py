def shift(str_two, str_one, q):
 
    if str_one == str_two: 
        return 0
 
    str_one += str_one
 
    a = 11
    b = 1
    s1hash = 0
    for i in str_two[::-1]:
        s1hash += ord(i) * b
        b *= a
        s1hash %= q
        b %= q
 
    b = 1
    hash = 0
    for i in str_one[:len(str_two)][::-1]:
        hash += b * ord(i)
        b *= a
        hash %= q
        b %= q
 
    hashtag = 1
    for i in range(len(str_two) - 1):
        hashtag *= a
        hashtag %= q
    for i in range(1, len(str_one) - len(str_two) + 1):
        hashnew = ((hash % q - ord(str_one[i - 1]) * hashtag % q) * a % q + ord(str_one[i + len(str_two) - 1])) % q
        if hashnew == s1hash:
            return i
        hash = hashnew

    return -1
 
string_one = input()
string_two = input()
q = 2 ** 31 - 1
print(shift(string_one, string_two, q))