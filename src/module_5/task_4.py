def task_4():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','0 0 2 0 1','5','1 5 2','2 4 2','3 5 3','1 1 1','3 4 1']))  # input
    >>> task_4()
    2 4 -1 1 4
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

    def GetSum(b, lt, rt, sTree, ql, qr):
        if ql <= lt and qr >= rt:
            return sTree[b]
        if ql >= rt or qr <= lt:
            return 0
        m = (rt+lt)//2
        sLt = GetSum(2*b+1, lt, m, sTree, ql, qr)
        sRt = GetSum(2*b+2, m, rt, sTree, ql, qr)
        return sLt + sRt
    def Main():
        num = int(input())
        a = [0 if int(i) != 0 else 1 for i in input().split()]
        sTree = [0]*4*num
        Build(0, 0, num, sTree, a)
        q = int(input())
        indx = []
        while q != 0:
            lt, rt, k = map(int, input().split())
            sum = GetSum(0, 0, num, sTree, lt-1, rt)
            if sum >= k and lt > 1:
                indx.append(Search(0, 0, num, sTree, k+GetSum(0, 0, num, sTree, 0, lt-1)))
            elif sum >= k and lt == 1:
                indx.append(Search(0, 0, num, sTree, k))
            else:
                indx.append(-1)
            q -= 1
        print(*indx)
    Main()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)