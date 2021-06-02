def func(c):
    mass=[0]*len(c)
    m = a =0
    for i in range(1, len(c)):
        if i <= a:
            mass[i] = min(mass[i-m], a-i+1)
        while mass[i] + i < len(c) and c[mass[i]] == c[mass[i]+i]:
            mass[i]= mass[i]+1
        if mass [i] + i - 1 > a:
            m=i
            a = mass[i] + i - 1
    return mass

def main():
    c = input()
    t = input()
    s = func(t+"#" + c)
    for i in range(len(s)):
        if len(t) == s[i]:
            print(i- len(t) - 1, end = " ")

main()