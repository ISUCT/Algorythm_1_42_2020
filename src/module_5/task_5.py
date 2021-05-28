def task_5():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','2 8 4 16 12','5','s 1 5','s 4 5','u 3 32','s 2 5','s 3 3']))  # input
    >>> task_5()
    2 4 4 32
    """
    from math import gcd

    def Build(b, lt, rt, sTree, a):
        if rt-lt == 1:
            sTree[b] = a[lt]
            return
        m = (lt+rt)//2
        Build(2*b + 1, lt, m, sTree, a)
        Build(2*b + 2, m, rt, sTree, a)
        sTree[b] = gcd(sTree[2*b + 1], sTree[2*b + 2])

    def GetGCD(b, lt, rt, sTree, qLt, qRt):
        if qLt <= lt and qRt >= rt:
            return sTree[b]
        if qLt >= rt or qRt <= lt:
            return 0
        m = (rt+lt)//2
        s_left = GetGCD(2*b+1, lt, m, sTree, qLt, qRt)
        s_right = GetGCD(2*b+2, m, rt, sTree, qLt, qRt)
        return gcd(s_left, s_right)

    def Up(b, lt, rt, sTree, indx, val):
        if rt-lt == 1:
            sTree[b] = val
            return
        m = (rt+lt)//2
        if indx < m:
            Up(2*b+1, lt, m, sTree, indx, val)
        else:
            Up(2*b+2, m, rt, sTree, indx, val)
        sTree[b] = gcd(sTree[2*b + 1], sTree[2*b + 2])

    def Main():
        nums = int(input())
        segTree = [0]*4*nums
        a = list(map(int, input().split()))[:nums]
        Build(0, 0, nums, segTree, a)
        q = int(input())
        rst = []
        while q != 0:
            que, l, r = map(str, input().split())
            if que=="s":
                rst.append(GetGCD(0, 0, nums, segTree, int(l)-1, int(r)))
            else:
                Up(0, 0, nums, segTree, int(l)-1, int(r))
            q -= 1
        print(*rst)
    Main()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)