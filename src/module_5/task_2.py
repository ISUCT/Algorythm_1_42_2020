def task_2():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7 3 2 1 9 5 4 6 8 0']))  # input
    >>> task_2()
    YES
    """
    class Node:  
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def Add(self, data):
            if data == self.data:
                return
            if data < self.data:
                if self.left:
                    self.left.Add(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.Add(data)
                else:
                    self.right = Node(data)

    def Height(tree):
        if tree is None:
            return 0
        return max(Height(tree.left), Height(tree.right))+1

    def Build(el):
        root = Node(el[0])
        for i in range(1, len(el)):
            root.Add(el[i])
        return root

    def Blnc(tree):
        if not tree or ((Height(tree.left) == Height(tree.right) or Height(tree.left)+1 == Height(tree.right) or Height(tree.left) == Height(tree.right)+1) 
        and Blnc(tree.right) and Blnc(tree.left)):
            return 1
        return 0

    def Main():
        n = list(map(int,input().split()))
        n.pop()
        tree = Build(n)

        if Blnc(tree) == 1: 
            print("YES")
        else:
            print("NO")
    Main()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)