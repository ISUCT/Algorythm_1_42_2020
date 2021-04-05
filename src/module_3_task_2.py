def hash_fun(s,q,p):
    hash = 0
    for i in range(len(s)):
        hash = (hash*q+ord(s[i]))%p
    return hash

def function(s,t,q,p):
    if s!=t:
        n = 1
        t = t[1:] + t[0]
        s_h = hash_fun(s,q,p)
        t_h = hash_fun(t,q,p)
        k = 1
        for i in range(len(s)-1):
            k=(k*q)%p
        for i in range(len(t)-1):
            if s_h == t_h:
                break
            else:
                t_h = (q*(t_h-ord(t[i])*k) + ord(t[i]))%p
                n += 1
        if s_h == t_h:
            print(n)
        else:
            print(-1)
    else:
        print(0)

def main():
    s = input() 
    t = input() 
    q = 30
    p = 1e9+6
    a = function(s,t,q,p)

main()