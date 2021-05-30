class key:
    __size = 0
    __height = 0

    def __init__(trees, leaf):
        trees.leaf = leaf
        trees.left = None
        trees.right = None
        key.__size += 1

    @property
    def size(trees):
        return trees.__size

    @property
    def height(trees):
        return trees.__height

    def add(trees, meaning, elevation):
        if trees.leaf == meaning:
            return
        if meaning < trees.leaf:
            if trees.left:
                trees.left.add(meaning, elevation+1)
            else:
                if key.__height < elevation:
                    key.__height = elevation
                trees.left = key(meaning)
        else:
            if trees.right:
                trees.right.add(meaning, elevation+1)
            else:
                if key.__height < elevation:
                    key.__height = elevation
                trees.right = key(meaning)

    def find_divarication(trees):
        if trees.left:
            trees.left.find_divarication()
        if trees.left and not trees.right:
            print(trees.leaf)
        if trees.right and not trees.left:
            print(trees.leaf)
        if trees.right:
            trees.right.find_divarication()

def binary_tree(objct):
    tree = key(objct[0])
    for i in range(1, len(objct)-1):
        tree.add(objct[i], 1)
    return tree

lisst = list(map(int, input().split()))
tree = binary_tree(lisst)
tree.find_divarication()