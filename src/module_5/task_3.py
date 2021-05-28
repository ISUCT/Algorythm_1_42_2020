def task_3():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','2 2 2 1 5','2','2 3','2 5']))  # input
    >>> task_3()
    2 1
    """
    def Build(b, lt, rt, sThree, num):
        if rt - lt == 1:
            sThree[b] = num[lt]
            return
        m = (rt + lt) // 2
        Build(2 * b + 1, lt, m, sThree, num)
        Build(2 * b + 2, m, rt, sThree, num)
        sThree[b] = NOD(sThree[2 * b + 1], sThree[2 * b + 2])

    def NOD(a,b):
        while b:
            a, b = b, a%b
        return a

    def GetNOD(b, lt, rt, sThree, Lt, Rt):
        if Lt <= lt and Rt >= rt:
            return sThree[b]
        if Lt >= rt or Rt <= lt:
            return 0
        m = (rt + lt) // 2
        stLt = GetNOD(2 * b + 1, lt, m, sThree, Lt, Rt)
        stRt = GetNOD(2 * b + 2, m, rt, sThree, Lt, Rt)
        return NOD(stLt, stRt)

    def Main():
        n = int(input())
        lst = list(map(int, input().split()))[:n]
        sThree = [0] * 4 * n 
        Build(0, 0, n, sThree, lst)
        q = int(input())
        a = []

        while q != 0:
            lt, rt = map(int, input().split())
            a.append(GetNOD(0, 0, n, sThree, lt - 1, rt))
            q -= 1
        print(*a)
    Main()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)