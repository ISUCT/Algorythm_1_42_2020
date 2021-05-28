def task_6():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','0 0 3 0 2','3','u 1 5','u 1 0','s 1 5 3']))  # input
    >>> task_6()
    4
    """
    def Build(b, lt, rt, sTree, a):
        if rt-lt == 1:
            sTree[b] = a[lt]
            return
        m = (rt+lt)//2
        Build(2*b+1, lt, m, sTree, a)
        Build(2*b+2, m, rt, sTree, a)
        sTree[b] = sTree[2*b+1] + sTree[2*b+2]

    def Search(b, lt, rt, sTree, k):
        if k > sTree[b]:
            return -1
        if rt - lt == 1:
            return rt
        m = (rt+lt)//2
        if sTree[2*b+1] >= k:
            return Search(2*b+1, lt, m, sTree, k)
        else:
            return Search(2*b+2, m, rt, sTree, k - sTree[2*b+1])

    def GetSum(b, lt, rt, sTree, Lt, Rt):
        if Lt <= lt and Rt >= rt:
            return sTree[b]
        if Lt >= rt or Rt <= lt:
            return 0
        m = (rt+lt)//2
        tLt = GetSum(2*b+1, lt, m, sTree, Lt, Rt)
        tRt = GetSum(2*b+2, m, rt, sTree, Lt, Rt)
        return tLt + tRt

    def Up(b, lt, rt, sTree, indxNew, value):
        if rt-lt == 1:
            sTree[b] = value
            return
        m = (rt+lt)//2
        if indxNew < m:
            Up(2*b+1, lt, m, sTree, indxNew, value)
        else:
            Up(2*b+2, m, rt, sTree, indxNew, value)
        sTree[b] = sTree[2*b+1] + sTree[2*b+2]
    def Main():
        n = int(input())
        a = [0 if int(i) != 0 else 1 for i in input().split()]
        sTree = [0]*4*n
        Build(0, 0, n, sTree, a)
        q = int(input())
        indx = []
        while q != 0:
            i = input().split()
            if len(i) == 4:
                lef, righ, k = int(i[1]), int(i[2]), int(i[3])
                sum = GetSum(0, 0, n, sTree, lef-1, righ)
                if sum >= k and lef > 1:
                    indx.append(Search(0, 0, n, sTree, k+GetSum(0, 0, n, sTree, 0, lef-1)))
                elif sum >= k and lef == 1:
                    indx.append(Search(0, 0, n, sTree, k))
                else:
                    indx.append(-1)
            else:
                i, b = int(i[1]), int(i[2])
                if b == 0:
                    Up(0, 0, n, sTree, i-1, 1)
                else:
                    Up(0, 0, n, sTree, i-1, 0)
            q -= 1
        print(*indx)
    Main() 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)