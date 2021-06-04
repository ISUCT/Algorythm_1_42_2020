def sdvig(s, t, q):
    if s==t:
        return 0
    else:
        t*=2
        p = 11
        m = 1
        sh = 0
        for i in s[::-1]:
            sh += ord(i) * m
            m *= p
            sh %= q
            m %= q

        m = 1
        hash = 0
        for i in t[:len(s)][::-1]:
            hash += m * ord(i)
            m *= p
            hash %= q
            m %= q

        ht = 1
        for i in range(len(s) - 1):
            ht *= p
            ht %= q
        for i in range(1, len(t) - len(s) + 1):
            hn = ((hash % q - ord(t[i - 1]) * ht % q) * p % q + ord(t[i + len(s) - 1])) % q
            if hn == sh:
                return i
            hash = hn

        return -1

s = input()
t = input()
q = 2**31 - 1
print(sdvig(s,t,q))

