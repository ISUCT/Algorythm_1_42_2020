def cyclic_shift(a,b,c):
    hash = 0
    for i in range(len(a)):
        hash = (hash*b+ord(a[i]))%c
    return hash

def function(a,t,b,c):
    if a!=t:
        mass = 1
        t = t[1:] + t[0]
        c_s = cyclic_shift(a,b,c)
        t_s = cyclic_shift(t,b,c)
        k = 1
        for i in range(len(a)-1):
            k=(k*b)%c
        for i in range(len(t)-1):
            if c_s == t_s:
                break
            else:
                t_s = (b*(t_s-ord(t[i])*k) + ord(t[i]))%c
                mass= mass+1
        if c_s == t_s:
            print(mass)
        else:
            print(-1)
    else:
        print(0)

def main():
    a = input() 
    t = input() 
    b = 30
    c = 1e9+6
    a = function(a,t,b,c)

main() 
