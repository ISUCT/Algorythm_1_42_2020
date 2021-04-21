def substring_search(m):
    S = [0]*len(m)
    for i in range(len(m) - 1):
        j = S[i]
        while j > 0 and (m[i+1] != m[j]):
            j = S[j-1]
        if m[i+1] == m[j]:
            S[i+1] = j+1
        else:
            S[i+1] = 0
    return S

def main():
    k = input()
    t = input()
    t_k = t + '&' + k
    S = substring_search(t_k)
    for i in range(len(S)):
        if S[i] == len(t):
            print(i-2*len(t), end = ' ')

main()