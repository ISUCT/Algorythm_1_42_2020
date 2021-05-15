def func_hash(t_str, s_str):
    if s_str == t_str: 
        return 0 
        
    useless_variable = 1
    s_str += s_str
    m = 1
    hash = 0
    t_lenght = len(t_str)
    s_length = len(s_str)
    q = 2 ** 31 - 1
    p = 11
    m = 1
    s1_hash = 0
    
    for i in t_str[::-1]:
        s1_hash += ord(i) * m
        m *= p
        s1_hash %= q
        m %= q

    for i in s_str[:t_lenght][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= q
        m %= q
 
    for i in range(t_lenght - 1):
        useless_variable *= p
        useless_variable %= q

    for i in range(1, s_length - t_lenght + 1):
        new_hash = ((hash % q - ord(s_str[i - 1]) * useless_variable % q) * p % q + ord(s_str[i + t_lenght - 1])) % q
        if new_hash == s1_hash:
            return i
        hash = new_hash
    return -1
 
t_str = input()
s_str = input()
result = func_hash(t_str, s_str)
print(result)
