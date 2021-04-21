def cyclic_shift(c,x,y):
    hash = 0
    for i in range(len(c)):
        hash = (hash*x+ord(c[i]))%y
    return hash

def function(c,t,x,y):
    if c!=t:
        arr = 1
        t = t[1:] + t[0]
        c_s = cyclic_shift(c,x,y)
        t_s = cyclic_shift(t,x,y)
        k = 1
        for i in range(len(c)-1):
            k=(k*x)%y
        for i in range(len(t)-1):
            if c_s == t_s:
                break
            else:
                t_s = (x*(t_s-ord(t[i])*k) + ord(t[i]))%y
                arr += 1
        if c_s == t_s:
            print(arr)
        else:
            print(-1)
    else:
        print(0)

def main():
    c = input() 
    t = input() 
    x = 30
    y = 1e9+6
    a = function(c,t,x,y)

main()